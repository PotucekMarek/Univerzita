#ifndef UTHREADS_H
#define UTHREADS_H

#include <stdint.h>

#define UTHREAD_JOINABLE	(1)
#define UTHREAD_DETACHED	(2)


/** mozne stavy vlakna */
enum uthread_status
{
	UT_NEW, UT_READY, UT_RUNNING, UT_BLOCKED, UT_TERMINATED
};

/** fronta vlaken realizovana jako oboustranny spojovy seznam */
struct uthread_queue
{
      struct uthread_tcb *head;
      struct uthread_tcb *tail;
};


/** struktura definujici vsechny vlasnosti vlakna */
struct uthread_tcb {
	// kontext vlakna
	uint64_t rip;
	uint64_t rsp;

	// callee-saved registry
	uint64_t rbp;
	uint64_t rbx;
	uint64_t r12;
	uint64_t r13;
	uint64_t r14;
	uint64_t r15;

	// servisni informace
	void *(*thread_proc)(void *arg); // funkce vykonavana vlaknem
	void *stack;                     // zacatek zasobniku
	void *arg;                       // predany argument
	void *result;                    // vysledna hodnota
	uint32_t id;                     // identifikator vlakna
	uint8_t attrs;                   // vlastnosti vlakna
	enum uthread_status status;      // stav vlakna

	// slouzi k umisteni vlakna do oboustranneho spojoveho seznamu (napr. fronty)
	struct uthread_tcb *prev;
	struct uthread_tcb *next;

	// ukazatel na vlakno, ktere ceka na dokonceni tohoto vlakna
	struct uthread_tcb *blocked_thread;

	// informace pro planovac
	uint64_t runtime;                // cas, po ktery vlakno bezelo
};


/** struktura definujici semafor */
struct uthread_sem
{
	int value;                            // hodnota semaforu, pokud je hodnota < 0, znamena to pocet cekajicich vlaken 
	struct uthread_queue blocked_threads; // fronta vlaken cekajicich na semaforu
};

typedef struct uthread_sem uthread_sem_t;

/**
 * Datovy typ urcujici vsechny vlasnosti vlakna.
 * Alias pro struct uthread_tcb, aby rozhrani bylo mozne pripadne zmenit.
 */
typedef struct uthread_tcb *uthread_t;


/* prepne aktualni vlakno a zacne provadet jine */
void uthread_yield();

/** vytvori nove vlakno, rozhrani kopiruje pthreads */
uthread_t uthread_create(void * (*thr_proc)(void *), int attributes, void *arg);

/** pocka na dobehnuti vlakna thread a pres argument result vrati navratovou hodnotu */
void uthread_join(uthread_t thread, void **result);

/** spusti planovac vlaken */
void uthread_start_scheduler(); 


/** inicializuje semafor */
void uthread_sem_init(uthread_sem_t *sem, int value);

/** snizi hodnotu semaforu o jedna, a pokud je uz na nule, tak ceka */
void uthread_sem_wait(uthread_sem_t *sem);

/** zvysi hodnotu semaforu o jedna, a pokud nejake vlakno na nej ceka, probudi jej  */
void uthread_sem_post(uthread_sem_t *sem);


#endif

