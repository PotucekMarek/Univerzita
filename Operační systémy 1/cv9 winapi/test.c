#include <stdio.h>
#include <unistd.h>

/**
int main() {
    while (1) {
        pid_t pid = getpid();

        printf("PID je: %d\n", pid);
    }

    return 0;
}*/
int main() {
    pid_t pid = fork();

    if (pid < 0) {
        return 1;  //error
    }

    else if (pid == 0) {
        printf("potomek PID: %d jeho rodič má PID: %d\n", getpid(), getppid()); 
        char *exec[] = {"uname", "--all", NULL};
        execv(exec[0], exec);
        return 1;
    } 

    else {
        printf("rodič PID: %d a jeho potomek má PID: %d\n", getpid(), pid);
        while (1) {
            sleep(1);
        }
    }

    return 0;
}