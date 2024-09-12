#include "uthreads-util.h"

/** inicializuje frontu vlaken */
void uthread_queue_init(struct uthread_queue *queue)
{
	queue->head = NULL;
	queue->tail = NULL;
}

/** vraci prvni vlakno ve fronte, pokud neexistuje, vraci NULL */
struct uthread_tcb *uthread_queue_poll(struct uthread_queue *queue)
{
	if (queue->head == NULL) return NULL;

	struct uthread_tcb *result = queue->head;
	queue->head = result->prev;
	if (queue->head == NULL) queue->tail = NULL;
	return result;
}

/** vlozi prvek do fronty vlaken */
void uthread_queue_put(struct uthread_queue *queue, struct uthread_tcb *thread)
{
	if (queue->head == NULL) {
		queue->head = thread;
		queue->tail = thread;
		thread->prev = NULL;
		thread->next = NULL;
	} else {
		queue->tail->prev = thread;
		thread->next = queue->tail;
		thread->prev = NULL;
		queue->tail = thread;
	}
}
