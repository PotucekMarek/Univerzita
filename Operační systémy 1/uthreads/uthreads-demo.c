#include <stdio.h>
#include "uthreads.h"
#define INT_TO_PTR(x)	((void *) ((long) x))

void *foo_thread(void *arg)
{
	printf("Spusteno vlakno A\n");
	int step = (long) arg;
	for (int i = 0; i < 10; i++) {
		printf("A:%i\n", i * step);
		uthread_yield();
	}
	return 0;
}

void *baz_thread(void *arg)
{
	printf("Spusteno vlakno C\n");
	for (int i = 0; i < 6; i++) {
		printf("C:%i\n", i);
		uthread_yield();
	}
	return INT_TO_PTR(42);;
}

void *bar_thread(void *arg)
{
	void *res;
	printf("Spusteno vlakno B\n");
	uthread_t thr3 = uthread_create(&baz_thread, UTHREAD_JOINABLE, NULL); 
	for (int i = 0; i < 5; i++) {
		printf("B:%i\n", i);
		uthread_yield();
	}

	printf("B ceka na C\n");
	uthread_join(thr3, &res);
	printf("C vratilo hodnotu %li\n", (long) res);

	for (int i = 5; i < 10; i++) {
		printf("B:%i\n", i);
		uthread_yield();
	}

	return NULL;
}

int main()
{
	uthread_t thr1 = uthread_create(&foo_thread, UTHREAD_DETACHED, INT_TO_PTR(1));
	uthread_t thr2 = uthread_create(&bar_thread, UTHREAD_DETACHED, INT_TO_PTR(2));

	printf("spustim vlakna ...\n");
	uthread_start_scheduler();
	printf("pokracuje se jiz bez vlaken\n");

	return 0;
}

