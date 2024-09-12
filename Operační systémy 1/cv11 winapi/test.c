#include <stdio.h>
#include <pthread.h>
#include <time.h>
#define COUNT (20)

static void msleep(int ms)
{
struct timespec t;
t.tv_sec = ms / 1000;
t.tv_nsec = (ms % 1000) * 1000000;
nanosleep(&t, NULL);
}

static void *thread_func(void *arg){
    int id = *((int *) arg);
    printf("Spusteno vlakno: %i\n", id);
    for (int i = 0; i < COUNT; i++) {
        printf("thr #%i: %i\n", id, i);
        msleep(5); 
    }
    return (void *) 42;
}
int main() {
    int id = 1;
    long result;
    pthread_t thread;
    if (pthread_create(&thread, NULL, thread_func, &id)) {
        fprintf(stderr, "Vytvoreni vlakna selhalo\n");
        return 1;
    }
    for (int i = 0; i < COUNT; i++) {
        printf("thr #main: %i\n", i);
        msleep(5);
    }
    pthread_join(thread, (void **) &result);
    printf("Result: %li\n", result);
    return 0;
}
