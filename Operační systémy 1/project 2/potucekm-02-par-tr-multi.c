#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef  __linux__
#include <pthread.h>
#endif

#ifdef _WIN32
#include <windows.h>
#include <tchar.h>
#include <strsafe.h>
#endif // _WIN32

#define inputSize 4096

#ifdef  __linux__
#define umain main
#define uchar char
#define strToInt atoi
#define uthread pthread_t
#define ulen strlen
#define ucmp(a, b) strcmp(a, b)
#define utype static void*
#define uparam void*
#define uprintStr(str) printf("%s", (str))
#define ucat strcat
#define ugetchar getchar
#define uprintf(f) printf(f);
#define UEOF EOF
#endif

#ifdef _WIN32
#define umain _tmain
#define uchar TCHAR
#define strToInt _tstoi
#define ulen _tcslen
#define ucmp(a, b) _tcscmp((_T(a)),(b))
#define uthread HANDLE
#define utype DWORD WINAPI
#define uparam LPVOID
#define uprintStr(str) (_tprintf(_T("%s"), (str))) 
#define ucat _tcscat
#define ustrncpy _tcsncpy
#define uint DWORD
#define ugetchar _gettchar
#define uprintf(f) _tprintf(_T(f));
#define UEOF _TEOF
#endif // _WIN32

/* deklarace pro mozne volani */
utype doTheStuff(uparam arg);

uchar* readStdin() {
    /* cte vstup z stdin
     * vraci:
     *  NULL: pokud doslo k chybe alokaci pameti
     *  referenci na input pokud nenastala chyba
     */

    int size = sizeof(uchar) * inputSize;
    uchar* input = (uchar *) malloc(size);

    if (input == NULL) {
        return NULL;
    }

    int i = 0;
    uchar ch = ugetchar();

    while (ch != UEOF) {
        if ((i + 1) == size) {
            size += inputSize;
            input = (uchar *) realloc(input, size);
            if (input == NULL) {
                return NULL;
            }
        }
        input[i++] = ch;
        ch = ugetchar();
    }

    input[i] = '\0';
    return input;
}

struct params {
    int delete;
    int change;
    int from;
    int to;
    uchar *input;
    uchar *oldSymbols;
    uchar *newSymbols;
    uchar *toDelete;
    uchar *deletedArray;
};

uint createdThreads(uthread *threads, struct params *pArr, int threadCount) {
    int i;
#ifdef __unix__
    for (i = 0; i < threadCount; ++i) {

        if (pthread_create(&threads[i], NULL, doTheStuff, &pArr[i])) {
            fprintf(stderr, "Vytvoreni vlakna selhalo\n");
            return 1;
        }
    }
    for (i = 0; i < threadCount; ++i) {
        pthread_join(threads[i], NULL);
    }
#endif

#ifdef _WIN32
    for (i = 0; i < threadCount; ++i) {
        threads[i] = CreateThread(NULL, 0, doTheStuff, &pArr[i], 0, NULL);

        if (threads[i] == NULL)
        {
            uprintStr("Vytvoreni vlakna selhalo\n");
            ExitProcess(1);
        }
    }

    for (i = 0; i < threadCount; ++i) {
        WaitForSingleObject(threads[i], INFINITE);
        CloseHandle(threads[i]);
    }


#endif // _WIN32
    return 0;
}


void changeSymbols(uchar *input, int from, int to, uchar *oldSymbols, uchar *newSymbols) {
    int i, j;
    for (i = from; i <= to; ++i) {
        for (j = 0; oldSymbols[j] != '\0'; ++j) {
            if (oldSymbols[j] == input[i]) {
                input[i] = newSymbols[j];
            }
        }
    }
}

void deleteSymbols(uchar input[], int from, int to, uchar toDelete[], uchar result[]) {
    int i, j, k = 0;
    for (i = from; i <= to; ++i) {
        for (j = 0; toDelete[j] != '\0'; ++j) {
            if (input[i] == toDelete[j]) {
                break;
            }
            if (toDelete[j + 1] == '\0') {
                result[k++] = input[i];
            }
        }
    }
    result[k] = '\0';
}

utype doTheStuff(uparam arg) {
    struct params *p = ((struct params *) arg);

    if (p->change) {
        changeSymbols(p->input, p->from, p->to, p->oldSymbols, p->newSymbols);
    }

    if (p->delete) {
        deleteSymbols(p->input, p->from, p->to, p->toDelete, p->deletedArray);
    }

    return NULL;
}

void resultRepair(uchar input[], uchar **deletedArray, int t_count) {
    input[0] = '\0';
    for (size_t i = 0; i < t_count; i++) {
        ucat(input, deletedArray[i]);
    }
}

void fillArgs(struct params *pArr, int threadCount, int countPerThread, int inputLen, uchar *input,
              uchar *oldSymbols, uchar *newSymbols, uchar *delArr, int change, int del, uchar **deletedArr) {
    int i;
    for (i = 0; i < threadCount; i++) {
        pArr[i].input = input;
        pArr[i].oldSymbols = oldSymbols;
        pArr[i].newSymbols = newSymbols;
        pArr[i].toDelete = delArr;
        pArr[i].change = change;
        pArr[i].delete = del;
        pArr[i].deletedArray = deletedArr[i];

        if (i == 0) {
            pArr[i].from = 0;
        } else {
            pArr[i].from = pArr[i - 1].from + countPerThread;
        }

        if ((i + 1) == threadCount) {
            pArr[i].to = inputLen - 1;

        } else {
            pArr[i].to = pArr[i].from + countPerThread - 1;
        }
    }
}

int umain(int argc, uchar *argv[]) {
    /* promenne */
    int threadCount = 1;
    int currentTested = 1;
    int delete = 0;
    int change = 0;
    uchar *delArr = NULL;
    uchar *oldSymbols = NULL;
    uchar *newSymbols = NULL;
    uchar **deletedArray = NULL;
    struct params *pArr = NULL;
    int inputLen;
    int countPerThread;
    int i;
    uchar *input = NULL;
    /* nacte stdin */
    input = readStdin();

    if (input == NULL) {
        uprintf("Chyba alokace pameti\n");
        return 1;
    }

    /* pripad kdy na vstupu nejsou zadne parametry */
    if (argc < 2) {
        uprintStr(input);
        return 0;
    }

    /* kontrola parametru */

    // pokud je parametr -t
    if (ucmp("-t", argv[currentTested]) == 0) {
        threadCount = strToInt(argv[2]);
        currentTested += 2;
    }

    // pokud je parametr -d
    if ((currentTested < argc) && (ucmp("-d", argv[currentTested]) == 0)) {
        delete = 1;
        delArr = argv[currentTested + 1];
        currentTested += 2;
    }

    // pokud je zmena znaku
    if (currentTested < argc) {
        change = 1;
        oldSymbols = argv[currentTested++];
        newSymbols = argv[currentTested++];
        currentTested += 2;
    }

    // opetovna kontrola -d pro prid opacneho poradi, dojde k overidu pokud v obou
    if ((currentTested < argc) && (ucmp("-d", argv[currentTested]) == 0)) {
        delete = 1;
        delArr = argv[currentTested + 1];
        currentTested += 2;
    }
    // alokace pole pro parametry vlaken
    pArr = (struct params *) malloc(threadCount * sizeof(struct params));

    /* kalkulace kolik kazde vlakno zpraceuje dat*/
    inputLen = ulen(input);
    countPerThread = inputLen / threadCount;

    /* alokace pole pro mazani */
    deletedArray = (uchar **) calloc(threadCount, sizeof(uchar *));


    for (i = 0; i < threadCount; i++) {
        deletedArray[i] = (uchar *) calloc((countPerThread * 10) + 1, sizeof(uchar));
    }

    /* plneni argumentu vlaken */
    fillArgs(pArr, threadCount, countPerThread, inputLen, input, oldSymbols, newSymbols, delArr, change, delete,
             deletedArray);

    /* pole vlaken*/
    uthread *threads = (uthread *) malloc(threadCount * sizeof(uthread));

    /* vytvoreni vlaken */
    if (createdThreads(threads, pArr, threadCount)) {
        return 1;
    }

    /* pokud se mazalo oprava vstupu */
    if (delete) {
        resultRepair(input, deletedArray, threadCount);
    }

    /* tisk vstupu */
    uprintStr(input);

    /* uvolneni poli */
    free(threads);
    free(pArr);

    for (i = 0; i < threadCount; i++) {
        free(deletedArray[i]);
    }

    free(deletedArray);
    free(input);

    return 0;
}