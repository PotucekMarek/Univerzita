#include <windows.h>
#include <tchar.h>

int _tmain(int argc, TCHAR* argv[]) {
    HANDLE hFile = CreateFile(
        _T("foo.txt"), // cesta k souboru
        GENERIC_READ | GENERIC_WRITE, // rezim prace se souborem
        FILE_SHARE_READ, // rezim sdileneho pristupu k souboru (pro cteni)
        NULL, // bezpecnostni atributy
        OPEN_ALWAYS, // jak nalozit s (ne)existujicimi soubory
        0, // priznaky souboru
        NULL); // odkaz na sablonu

    if (hFile == INVALID_HANDLE_VALUE) {
        _tprintf(_T("error opening file\n"));
        return -1;
    }

    _TCHAR* str = _T("Hello worl!");
    if (WriteFile(hFile, str, sizeof(_TCHAR) * _tcslen(str), NULL, NULL))
    _tprintf(_T("ok"));

    CloseHandle(hFile);
    return 0;
}