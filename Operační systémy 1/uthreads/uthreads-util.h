#ifndef UTHREADS_UTIL_H
#define UTHREADS_UTIL_H

#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include "uthreads.h"

/** inicializuje frontu vlaken */
void uthread_queue_init(struct uthread_queue *queue);

/** vraci prvni vlakno ve fronte, pokud neexistuje, vraci NULL */
struct uthread_tcb *uthread_queue_poll(struct uthread_queue *queue);

/** vlozi prvek do fronty vlaken */
void uthread_queue_put(struct uthread_queue *queue, struct uthread_tcb *thread);


/** vraci hodnotu casovace s nanosekundovou presnosti */
static inline uint64_t current_timestamp_ns()
{
	struct timespec ts;
	if (clock_gettime(CLOCK_MONOTONIC, &ts) < 0) abort();
	return ts.tv_sec * 1000000000 + ts.tv_nsec;
}
#endif
