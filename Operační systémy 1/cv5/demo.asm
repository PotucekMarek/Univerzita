section .text

global swap
global division
global countdown
global nasobky
global minimum
global my_strlen
global my_strcat

; Funkce swap
swap:
    mov eax, [rdi]     ; Načte hodnotu A (ukazatel rdi)
    mov edx, [rsi]     ; Načte hodnotu B (ukazatel rsi)
    mov [rdi], edx     ; Uloží hodnotu B na místo A
    mov [rsi], eax     ; Uloží hodnotu A na místo B
    ret

; Funkce division
division:
    mov eax, edi       ; x do eax
    xor edx, edx       ; Nuluje edx pro div
    div esi            ; eax / y, výsledek do eax, zbytek do edx
    mov [rdx + 16], eax; Uloží výsledek do paměti na adrese result
    mov [r8 + 24], edx ; Uloží zbytek do paměti na adrese remainder
    ret

; Funkce countdown
countdown:
    mov ecx, 10        ; Nastaví počítadlo na 10
.loop:
    mov [rdi], ecx     ; Uloží hodnotu ECX do paměti na adresu rdi
    add rdi, 4         ; Posune se na další místo v poli
    dec ecx            ; Decrement počítadlo
    jnz .loop          ; Dokud není ECX nulové, pokračuje
    ret

; Funkce nasobky
nasobky:
    xor rdx, rdx       ; Nuluje index rdx
.loop_mul:
    imul rax, rdx, rsi ; rax = rdx * n
    mov [rdi + rdx * 2], ax ; Uloží výsledek do pole
    inc rdx            ; Zvýší index
    cmp rdx, 10        ; Kontrola na 10 násobků
    jl .loop_mul       ; Pokračuje, pokud je méně než 10
    ret

; Funkce minimum
minimum:
    mov eax, [rsi]     ; Uloží první hodnotu do eax
    mov ecx, edi       ; Nastaví counter do ecx (count)
    xor rdx, rdx       ; Nuluje index
.loop_min:
    mov esi, [rsi + rdx * 4] ; Načte hodnotu z pole
    cmp esi, eax       ; Porovná aktuální minimum s další hodnotou
    jge .skip_min
    mov eax, esi       ; Pokud je hodnota menší, stane se novým minimem
.skip_min:
    inc rdx            ; Posune index
    cmp rdx, ecx       ; Porovná index s počtem prvků
    jl .loop_min       ; Pokračuje, pokud nejsou všechny hodnoty prošlé
    ret

; Funkce my_strlen
my_strlen:
    xor rcx, rcx       ; Nuluje čítač
.loop_strlen:
    cmp byte [rdi + rcx], 0 ; Porovná aktuální znak s nulou
    je .done_strlen     ; Pokud je to nula, ukončí cyklus
    inc rcx            ; Jinak zvýší čítač
    jmp .loop_strlen   ; A pokračuje dál
.done_strlen:
    mov rax, rcx       ; Délku uloží do rax
    ret

; Funkce my_strcat
my_strcat:
    ; Najde konec řetězce dest
    mov rax, rdi
.find_end:
    cmp byte [rax], 0
    je .concat_start
    inc rax
    jmp .find_end

.concat_start:
    mov rdx, rsi
.concat_loop:
    mov al, [rdx]
    test al, al
    je .concat_done
    mov [rax], al
    inc rax
    inc rdx
    jmp .concat_loop

.concat_done:
    mov byte [rax], 0
    ret