#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "uthreads.h"
#include "uthreads-util.h"

#define UTHREAD_STACK_SIZE	(0x10000)

/** ukazatel na aktualne bezici vlakno */
struct uthread_tcb *uthread_active_tcb = NULL;

/** fronta vlaken, ktere jsou pripraveny k behu */
static struct uthread_queue queue;

/** celkovy pocet vytvorenych vlaken */
static uint32_t threads_total = 0;

/** pocet vlaken ve stavu blocked */
static unsigned int blocked = 0;

/**
 * pomocna struktura, do ktere si ulozime kontext,
 * ze ktereho byla zavolana funkce uthread_start_scheduler,
 * abychom se do ni mohli vratit
 */
extern struct uthread_tcb uthread_mainthread_context;

/** spusti vlakno, ktere je nastaveno v uthread_active_tcb */
void uthread_run();

/** ulozi kontext vlakna do uthread_active_tcb a zavola uthread_switch */
void uthread_internal_yield(int block_current_thread);

//
//
// PLANOVAC VLAKEN
//
//

/** inicializuje planovac */
static void uthread_scheduler_init()
{
	uthread_queue_init(&queue);
}

/** 
 * funkce planovace, ktera vybere prvni cekajici vlakno
 * pokud je fronta prazdna vraci NULL
 */
static inline struct uthread_tcb *uthread_scheduler_dequeue()
{
	return uthread_queue_poll(&queue); 
}

/**
 * funkce planovace, ktera zaradi vlakno do fronty vlaken pripravenych k behu
 */
static inline void uthread_scheduler_enqueue(struct uthread_tcb *thread)
{
	uthread_queue_put(&queue, thread);
}

//
//
// FUNKCE OBSTARAVAJICI PREPINANI VLAKEN
//
//

/** prepne aktualni vlakno (prepnuti READY -> READY) */
void uthread_yield()
{
	uthread_internal_yield(0);
}

/** zablokuje aktualni vlakno a da provadet dalsi (prepnuti READY -> BLOCKED) */
static inline void uthread_block()
{
	uthread_internal_yield(1);
}

/** prepne vlakno ze stavu BLOCKED do stavu READY */
static inline void uthread_wakeup(struct uthread_tcb *thread)
{
	thread->status = UT_READY;
	blocked--;
	uthread_scheduler_enqueue(thread);
}

/** 
 * prepne z aktualniho vlakna na dalsi, argument udava,
 * jestli vlakno prechazi do stavu blocked (block_current_thread == 1)
 * nebo ready (block_current_thread == 0)
 */
void uthread_switch(int block_current_thread)
{
	static uint64_t thread_start; // obsahuje informaci o case, kdy dane vlakno bylo prepnuto do stavu RUNNING
	// pokud existuje aktivni vlakno, zaradime jej do fronty
	if (uthread_active_tcb) {
		// aktualizuje informaci o vyuzitem procesorovem case
		uthread_active_tcb->runtime += current_timestamp_ns() - thread_start;

		// zmena stavu a zarazeni do fronty
		if (!block_current_thread) { 
			uthread_active_tcb->status = UT_READY;
			uthread_scheduler_enqueue(uthread_active_tcb);
		} else {
			uthread_active_tcb->status = UT_BLOCKED;
			blocked++;
		}
	}

	// volba a aktivace noveho vlakna
	uthread_active_tcb = uthread_scheduler_dequeue();

	// pokud neexistuje dalsi vlakno, vracime se do funkce, ktera volala uthread_start_scheduler()
	if (!uthread_active_tcb) {
		if (blocked) {
			fprintf(stderr, "deadlock");
			abort();
		}
		uthread_active_tcb = &uthread_mainthread_context;
	}
	thread_start = current_timestamp_ns();
	uthread_run();
}

//
//
// FUNKCE MAJICI NA STAROST VYTVORENI A UKONCENI VLAKEN
//
//

void uthread_join(uthread_t thread, void **result);
uthread_t uthread_create(void * (*thr_proc)(void *), int attributes, void *arg);
static void uthread_wrapper();
static void uthread_dispose(struct uthread_tcb *thread);

/**
 * Vytvori nove vlakno reprezentovane funkci thr_proc a spusti jej s argumentem arg.
 * Jako atribut lze uvest bud UTHREAD_JOINABLE nebo UTHREAD_DETACHED, v druhem pripade
 * nelze volat funkci uthread_join a prostredky vlakna jsou uvoleny okamzite po jeho
 * dokonceni
 */
uthread_t uthread_create(void * (*thr_proc)(void *), int attributes, void *arg)
{
	// pri vytvoreni prvniho vlakna inicializujeme planovac
	if (threads_total == 0) uthread_scheduler_init();

	struct uthread_tcb *tcb   = malloc(sizeof(struct uthread_tcb));

	// vytvori zasobnik pro nove vytvorene vlakno
	unsigned char      *stack = malloc(UTHREAD_STACK_SIZE);

	tcb->rip            = (uint64_t) uthread_wrapper;              // nevolame primo funkci, ale obalovou funkci, ktera resi uvolneni prostredku a synchronizaci s ostatnimi vlakny
	tcb->rsp            = (uint64_t) (stack + UTHREAD_STACK_SIZE); // zasobnik roste od vyssich adres
	tcb->stack          = stack;
	tcb->id             = threads_total++;
	tcb->arg            = arg;
	tcb->thread_proc    = thr_proc;
	tcb->attrs          = attributes;
	tcb->blocked_thread = NULL;
	tcb->runtime        = 0;
	tcb->status         = UT_NEW;

	uthread_scheduler_enqueue(tcb);

	return tcb;
}

/**
 * obalova funkce, ktera se postara o spusteni kodu vlakna
 * a hlavne po jeho skonceni zaridi uvolneni zdroju/zarazeni
 * mezi zombie vlakna a prepnuti na dalsi vlakno
 */
static void uthread_wrapper()
{
	// spusti kod vlakna se zadanym argumentem
	void *result = uthread_active_tcb->thread_proc(uthread_active_tcb->arg);

	// resi uvolneni prostredku vlakna
	if (uthread_active_tcb->attrs & UTHREAD_DETACHED) {
		// uvolnime prostredky okamzite, jine vlakno neceka
		uthread_dispose(uthread_active_tcb);
	} else {
		// ulozime vysledek, a pokud existuje vlakno, ktere ceka na dokonceni
		// tohoto vlakna, probudime jej
		uthread_active_tcb->result = result;
		uthread_active_tcb->status = UT_TERMINATED;
		if (uthread_active_tcb->blocked_thread) {
			uthread_wakeup(uthread_active_tcb->blocked_thread);
		}
	}
	uthread_active_tcb = NULL;
	uthread_switch(0);
}

/** pocka na dokonceni zadaneho vlakna a prevezme od nej navratovou hodnotu */
void uthread_join(uthread_t thread, void **result)
{
	// pokud vlakno jeste nedobehlo, uspime aktualni vlakno
	if (thread->status != UT_TERMINATED) {
		thread->blocked_thread = uthread_active_tcb;
		uthread_block();
	}

	// vratime hodnotu a uvolnime prostredky
	if (result) {
		*result = thread->result;
	}
	uthread_dispose(thread);
}

/** uvolni struktury daneho vlakna */
static void uthread_dispose(struct uthread_tcb *thread)
{
	free(thread->stack);
	free(thread);
}

//
//
// IMPLEMENTACE SEMAFORU
//
//

/** inicializuje semafor */
void uthread_sem_init(uthread_sem_t *sem, int value)
{
	sem->value = value;
	uthread_queue_init(&sem->blocked_threads);
}

/** snizi hodnotu semaforu o jedna, a pokud je uz na nule, tak ceka */
void uthread_sem_wait(uthread_sem_t *sem)
{
	sem->value--;
	if (sem->value < 0) {
		uthread_queue_put(&sem->blocked_threads, uthread_active_tcb);
		uthread_block();
	}
}

/** zvysi hodnotu semaforu o jedna, a pokud nejake vlakno na nej ceka, probudi jej  */
void uthread_sem_post(uthread_sem_t *sem)
{
	if (sem->value < 0) {
		struct uthread_tcb *blocked = uthread_queue_poll(&sem->blocked_threads);
		uthread_wakeup(blocked);
	}
	sem->value++;

}
