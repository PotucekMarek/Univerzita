section .text

global print_row
global print_rect
global factorial
global my_strdup
global fib

extern putchar
extern malloc
extern free
extern strlen

; Funkce print_row
print_row:
    push rbx                ; Uložíme rbx
    mov ebx, edi            ; Přesuneme n do ebx
    mov al, dil             ; Znak c do al
.loop_row:
    test ebx, ebx           ; Test jestli je ebx > 0
    jz .done_row            ; Pokud je ebx == 0, skončíme
    mov edi, eax            ; Nastavíme znak pro volání putchar
    call putchar            ; Zavoláme putchar
    sub ebx, 1              ; Decrement n
    jmp .loop_row           ; Pokračujeme
.done_row:
    mov edi, 10             ; Vypíšeme nový řádek \n
    call putchar
    pop rbx                 ; Obnovíme rbx
    ret

; Funkce print_rect
print_rect:
    push rbx                ; Uložíme rbx
    mov ebx, edi            ; Přesuneme rows do ebx
.loop_rect:
    test ebx, ebx           ; Test jestli je ebx > 0
    jz .done_rect           ; Pokud je ebx == 0, skončíme
    mov edi, esi            ; Přeneseme cols do edi (počet sloupců)
    mov dil, '*'            ; Znak '*' pro výpis
    call print_row          ; Zavoláme print_row
    sub ebx, 1              ; Decrement rows
    jmp .loop_rect          ; Pokračujeme
.done_rect:
    pop rbx                 ; Obnovíme rbx
    ret

; Funkce factorial
factorial:
    cmp edi, 1              ; Pokud je n <= 1
    jbe .base_case          ; Vrátíme 1
    dec edi                 ; n = n - 1
    call factorial          ; Rekurzivní volání factorial(n-1)
    imul eax, edi + 1       ; Výsledek = n * factorial(n-1)
    ret
.base_case:
    mov eax, 1              ; Vracíme 1
    ret

; Funkce my_strdup
my_strdup:
    call strlen             ; Získáme délku řetězce
    inc rax                 ; Přidáme 1 na místo pro '\0'
    mov rdi, rax            ; Nastavíme velikost pro malloc
    call malloc             ; Alokujeme paměť
    test rax, rax           ; Testujeme, zda malloc uspěl
    jz .done_strdup         ; Pokud ne, vracíme NULL
    mov rdi, rsi            ; Nastavíme zdrojový řetězec
    mov rsi, rax            ; Nastavíme cíl pro kopii
.copy_loop:
    mov al, [rdi]           ; Načteme znak ze zdroje
    mov [rsi], al           ; Uložíme znak do cíle
    test al, al             ; Zkontrolujeme, zda jsme u konce řetězce
    je .done_strdup         ; Pokud ano, skončíme
    inc rdi                 ; Posuneme zdrojový ukazatel
    inc rsi                 ; Posuneme cíl
    jmp .copy_loop          ; Pokračujeme
.done_strdup:
    ret

; Funkce fib
fib:
    cmp di, 1               ; Pokud je n <= 1
    jbe .base_fib           ; Vrátíme n
    dec di                  ; n = n - 1
    mov rbx, rdi            ; Uložíme n do rbx
    call fib                ; fib(n-1)
    mov rdx, rax            ; Uložíme fib(n-1) do rdx
    dec rbx                 ; n = n - 2
    mov rdi, rbx            ; Připravíme n-2
    call fib                ; fib(n-2)
    add rax, rdx            ; Výsledek = fib(n-1) + fib(n-2)
    ret
.base_fib:
    mov eax, edi            ; Vrátíme n (0 nebo 1)
    ret