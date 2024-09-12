section .text

global signum
global max2c
global min3us
global mocnina

; prvni ukol
signum:
    cmp rdi, 0     ; porovná hodnotu s nulou
    jz zero        ; pokud je input nulo, skočí na zero
    mov eax, 1     ; nastaví eax na 1
    jl negative    ; pokud je input mensi nez nula, skoci na negative
    ret            ; pokud je input vetsi nez nula, vrati 1
negative:
    mov eax, -1    ; nastavi eax na -1
    ret
zero:
    xor eax, eax   ; nastavi eax na 0
    ret

; druhy ukol
max2c:
	mov eax, edi    ; vloží input do eax
	cmp edi, esi    ; porovná hodnotu s edi
	jg first        ; jestli je hodnota edi vetsi nez hodnota druheho znaku skoci na first 
	mov eax, esi    ; jestli ne, vlozi druhou hodnotu do eax
	ret

first:
	ret

; paty ukol
mocnina:
    mov eax, 1      ; do eax vloz 1
    cmp esi, 0      ; porovnej hodnotu s 0
    jg nasob        ; skoc do nasob, jeslti jestli je hodnota vetsi nez 0
    ret

nasob:
    imul eax, edi   ; vynasobi obe hodnoty
	add esi, -1     ; odecte -1
    cmp esi, 0      ; porovna hodnotu, jestli neni nula
    jg nasob        ; pokud je, skoci na zacatek
	ret