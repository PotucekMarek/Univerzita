#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
#include <tchar.h>
#include <windows.h>
#endif

#ifdef __unix__

#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

#endif

#define inputSize 4096

#ifdef _WIN32
#define uchar TCHAR
#define uint DWORD
#define fuint DWORD WINAPI
#define umain _tmain
#define ufopen _tfopen
#define ufgets _fgetts
#define uread _T("r")
#define uprintf(s)  _tprintf(_T("%s"), (s));
#define ugetchar _gettchar
#define ustrcat _tcscat
#define ufopen _tfopen
#endif

#ifdef __unix__
#define uchar char
#define uint int
#define fuint int
#define umain main
#define ufopen fopen
#define ufgets fgets
#define uread "r"
#define uprintf(s)  printf("%s", (s));
#define ugetchar getchar
#define ustrcat strcat
#define m 1024
#define n 512
#define ufopen fopen
#endif

struct param {
    uchar *AppName;
    uchar *Args;
};

#ifdef _WIN32
int ProcessFunc(LPVOID lpParam) {

    /* windows funkce pro vytvoreni procesu */

    struct param* p = (struct param*)lpParam;
    uint result;

    STARTUPINFO si;
    PROCESS_INFORMATION pi;

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));

    // Start the child process.
    if (!CreateProcess(
        NULL,           // No module name (use command line)
        p->Args,        // Command line
        NULL,           // Process handle not inheritable
        NULL,           // Thread handle not inheritable
        FALSE,          // Set handle inheritance to FALSE
        0,              // No creation flags
        NULL,           // Use parent's environment block
        NULL,           // Use parent's starting directory
        &si,            // Pointer to STARTUPINFO structure
        &pi)            // Pointer to PROCESS_INFORMATION structure
        )
    {
        _tprintf(_T("CreateProcess failed succefully (%d).\n"), GetLastError());
        return 1;
    }

    // Wait until child process exits.
    WaitForSingleObject(pi.hProcess, INFINITE);

    GetExitCodeProcess(&pi, &result);

    // Close process and thread handles.
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
    return result;
}
#endif

#ifdef __unix__

/* unix funkce pro vytvoreni procesu */

void ParseArgsForFork(uchar *args, uchar listOfArgs[m][n]) {
    int i, j = 0, k = 0;

    for (i = 0; i < n; ++i) {
        listOfArgs[i][0] = 0;
    }

    for (i = 0;; ++i) {

        if (args[i] == '\0') {
            listOfArgs[j][k] = 0;
            k = 0;
            j++;
            break;
        }

        if ((args[i] == ' ') || (args[i] == '\t')) {
            listOfArgs[j][k] = 0;
            k = 0;
            j++;
            continue;
        }
        listOfArgs[j][k++] = args[i];
    }
}

int ProcessFunc(struct param *args) {
    int returnStatus;
    int i;
    uchar function_args[m][n];
    uchar *functinonArgs[m];
    pid_t pid;

    /* pripravy argumenty po castech pro vytvareni procesu */
    ParseArgsForFork(args->Args, function_args);

    for (i = 0; function_args[i][0] != '\0'; ++i) {
        functinonArgs[i] = function_args[i];
    }
    functinonArgs[i] = NULL;

    /* vytvoreni potomka */
    pid = fork();

    if (pid == 0) { // kod potomka pokud vytvoreni potomka probehlo v poradku
        execvp(args->AppName, functinonArgs);
        exit(0);
    } else if (pid < 0) { // kod potomka pokud vytvoreni potomka neprobehlo v poradku
        printf("Chyba pri vytvareni forku\n");
        exit(1);
    } else { // kod rodice
        /* pocka na dokonceni potomka */
        if (waitpid(pid, &returnStatus, 0) == -1){ // kontrola jestli se cekalo
            printf("Chyba pri cekani na potomka\n");
            return 1;
        }

        /* pokud potomek skoncil normalne */
        if (WIFEXITED(returnStatus)) {
            /* navratova hodnota potomka */
            return WEXITSTATUS(returnStatus);
        }
        /* pokud byl potomek ukoncen signalem */
        if (WIFSIGNALED(returnStatus)) {
            /* navrat cisla signalu */
            return WTERMSIG(returnStatus);
        }
        return 1;
    }
}

#endif

int ParseFrom(uchar input[], int *from, uchar buffer[]) {

    /* navratove hodnoty
     *   funcke kopiruje obsah vstupu od indexu from do bufferu
     *   jakmile narazi na ukoncovaci znak tak vrati prislusnou hodnotu:
     *
     *   4: na vstupu je prazdny retezec, nebo uz jsme na konci retezce a nebylo nic zpracovano
     *   3: vstup konci ukoncovacim znakem stringu, ale bylo neco zpracovano
     *   2: vstup konci && -> informace pro volaci funci, aby kontrolovala navrat z procesu
     *   1: vstup konci ;
     *   0: vstup konci novym radkem
     */

    int j = 0;
    for (;; *from += 1) {
        if ((j == 0) && (input[*from] == '\0')) {
            return 4;
        }

        if (input[*from] == '\0') {
            buffer[j] = '\0';
            return 3;
        }

        if ((j == 0) && ((input[*from] == ' ') || (input[*from] == '\t'))) {
            continue;
        }

        if (input[*from] == '\n') {
            buffer[j] = '\0';
            *from += 1;
            return 0;
        }

        if (input[*from] == ';') {
            buffer[j] = '\0';
            *from += 1;
            return 1;
        }

        if ((input[*from] == '&') && (input[*from + 1] == '&')) {
            buffer[j] = '\0';
            *from += 2;
            return 2;
        }

        buffer[j++] = input[*from];
    }
}

void ParseAppName(uchar buffer[], uchar appName[]) {

    /* vyfiltruje nazev prikazu */

    for (size_t i = 0;; i++) {
        if ((buffer[i] == ' ') || (buffer[i] == '\0') || (buffer[i] == '\n') ||
            ((buffer[i] == '&') && (buffer[i + 1] == '&')) || (buffer[i] == '\t')) {
            appName[i] = '\0';
            return;
        }

        appName[i] = buffer[i];
    }
}

void ParseInput(uchar input[]) {

    /* vstup rozdeli na jmeno a jmeno + argumenty pro valany proces */

    uchar appName[n];
    uchar args[m];
    struct param *p = (struct param *) malloc(sizeof(struct param));

    int i = 0;
    int parseReturnedValue;
    int processReturnedValue;

    while (input[i] != '\0') {
        parseReturnedValue = ParseFrom(input, &i, args);

        ParseAppName(args, appName);

        p->Args = args;
        p->AppName = appName;
        processReturnedValue = ProcessFunc(p);

        if ((parseReturnedValue == 2) && (processReturnedValue != 0)) {
            while ((input[i] != ';') && (input[i] != '\n')) {
                i++;
            }
            i++;
        }
    }
    free(p);
}

int umain(int argc, uchar *argv[]) {
    /* deklarace promennych */
    FILE *fp;
    uchar input[inputSize];
    input[0] = '\0';

    uchar line[inputSize];
    line[0] = '\0';

    /* pokud na vstupu nic neni */
    if (argc < 2) {
        return 0;
    }

    /* otevreni vstupniho souboru pro cteni */
    fp = ufopen(argv[1], uread);

    /* pokud doslo k chybe */
    if (fp == NULL) {
        uprintf("File open error\n");
        return 1;
    }

    /* kopirovani obsahu souboru do pole input */
    while (ufgets(line, inputSize, fp)) {
        ustrcat(input, line);
    }

    /* uzavreni souboru */
    fclose(fp);

    /* pro testovaci ucely */
    //uchar input[] = "echo Operacni system je ; uname -o\nfalse && echo Toto se nevypise\necho Tento text se vypsal";
    //uchar input[] = _T("C:\\Windows\\System32\\cmd.exe /c echo haf ; C:\\Windows\\System32\\cmd.exe /c dir \n");
    //uchar input[] = _T("echo haf ; dir");
    //uchar input[] = _T("notepad.exe");

    /* zpracovani vstupu a zavolani procesu */
    ParseInput(input);
    return 0;
}