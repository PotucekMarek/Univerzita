#include <windows.h>
#include <tchar.h>
#include <stdio.h>

#define COUNT (20)
#define NUM_THREADS (6) // Zadejte počet vláken, se kterými chcete pracovat

DWORD WINAPI ThreadFunc(LPVOID lpParam) {
    _tprintf(_T("Spusteno vlakno s id: %i\n"), GetCurrentThreadId());
    DWORD x = *(DWORD *)lpParam;
    for (int i = 0; i < COUNT; i++) {
        _tprintf(_T("thr #%i: %i\n"), x, i);
    }
    return 0;
}

int _tmain() {
    DWORD dwThreadId[NUM_THREADS];
    DWORD dwThrdParam[NUM_THREADS];
    DWORD dwExitCode;
    HANDLE hThread[NUM_THREADS];

    for (int i = 0; i < NUM_THREADS; i++) {
        dwThrdParam[i] = i + 1;
        hThread[i] = CreateThread(
            NULL, // bezpecnostni atributy
            0, // velikost zasobniku (0 -> implicitni hodnota)
            ThreadFunc, // funkce provadena vlakna
            &dwThrdParam[i], // argument predany vlaknu
            0, // priznaky pro vytvorene vlakno
            &dwThreadId[i]); // vraci id vlakna

        if (hThread[i] == NULL) {
            _tprintf(_T("Vytvoreni vlakna %i selhalo\n"), i);
            ExitProcess(0);
        } else {
            _tprintf(_T("Vytvoreno vlakno %i s id: %i\n"), i, dwThreadId[i]);
        }
    }

    for (int i = 0; i < COUNT; i++) {
        _tprintf(_T("thr #0: %i\n"), i);
    }

    WaitForMultipleObjects(NUM_THREADS, hThread, TRUE, INFINITE); // ceka na skonceni vsech vlaken

    for (int i = 0; i < NUM_THREADS; i++) {
        if (GetExitCodeThread(hThread[i], &dwExitCode)) {
            _tprintf(_T("Vlakno %i ukonceno s kodem: %lu\n"), i, dwExitCode);
        } 
        else {
            _tprintf(_T("Nepodarilo se ziskat kod ukonceni vlakna %i\n"), i);
        }
        CloseHandle(hThread[i]); // ukonci praci s vlaknem
    }

    return 0;
}