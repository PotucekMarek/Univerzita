section .text

global format_str
global align_str
global typeset

format_str:
    mov rcx, 0 ; rcx pozoruje, zda se nacházíme mezi *
    mov rdx, 0 ; rcx pozoruje, zda se nacházíme mezi _

zpracuj:
    mov al, [rsi] ; do al se da character z rsi
    add rsi, 1
    cmp al, 0  ; jestliže je '\0' konci
    jz done
    cmp al, 42  ; jestli je znak * 
    jne oznac_podtrzitko
    cmp rcx, 0 ; jeslti je prvni  *
    jz prvni_hvezda
    mov rcx, 0 ; resetuje rcx, pokud je 2. *
    jmp buffer

prvni_hvezda: ; ulozi si, že jsme stale v *
    mov rcx, 1
    jmp buffer

oznac_podtrzitko:
    cmp al, 95 ; kontrola jestli je podtrzitko
    jne konvertuj
    cmp rdx, 0 ; kontrola, jestli je prvni _
    jz prvni_podtrzitko
    mov rdx, 0
    jmp buffer

prvni_podtrzitko: ; ulozi si, že jsme stale v _
    mov rdx, 1
    jmp buffer

konvertuj:
    cmp rcx, 0 ; jestli jsme mezi *
    jz konvert_podtrzitka
    cmp al, 97 ; 'a'
    jb buffer
    cmp al, 122 ; 'z'
    ja buffer
    sub al, 32 ; mezi 97-122 prevede na velke pismeno
    jmp buffer

konvert_podtrzitka:
    cmp rdx, 0 ; kontrola, pokud jsme mezai podtrzitky
    jz buffer
    cmp al, 32 ; je mezera?
    jne buffer
    mov al, 95 ; konvertuje podrtrzitko

buffer:
    mov [rdi], al
    add rdi, 1
    jmp zpracuj ; skoč na začatek

done:
    mov [rdi], al
    ret



align_str:
    ; rdx size, rdi output, rsi input 
    mov rbx, rcx; t
    cmp byte [rsi], 32 ; pokud prvni znak neni mezera
    jne spocitej_delku 
    add rsi, 1  ;  posune input na další char
    jmp align_str

spocitej_delku:  ; bez mezer na zacatku a na konci dokud nenarazi na nulovy byte
    cmp byte [rsi + rcx], 0 ; rsi-začatek(po odstraneni mezer), rcx-aktualni, kontroluje konec retezce
    je odstrani_konec ; jakmile dojde na konec stringu -> odstrani mezery na konci
    add rcx, 1 ; zvetsuje aktualni pozici -> pocita delku
    jmp spocitej_delku

odstrani_konec:
    cmp rcx, 0 ; pokud je delka retezce 0 -> neni nic k odstraneni
    je pocet_mezer 
    cmp byte [rsi + rcx - 1], 32  ; posledni znak stringu, rcx-1 protože indexace řetězce začína od 0
    jne pocet_mezer ; jestli neni mezera, skoc
    sub rcx, 1 ; pokud je znak mezera snizi delku retezce
    jmp odstrani_konec   

pocet_mezer:
    sub rdx, rcx ; rdc-velikost rcx-upraveny retezec -> kolik mezer pridat
    cmp rbx, 2 ; jaké bude zarovnání -> vpravo
    je na_pravo
    cmp rbx, 1 ; jaké bude zarovnání -> uprostred
    je na_stred  
    jmp mezery ; pokud je zarovnani vlevo

na_stred:
    sar rdx, 1 ; dělí mezery
    mov r13, rdx ; kolik je mezer, ktere se pridaji pred retezec
    jmp mezery

na_pravo:
    mov r13, rdx  ; kolik je mezer, ktere se pridaji pred retezec

mezery:
    cmp r13, 0 
    je output 
    mov byte [rdi], 32 ; prida mezeru
    add rdi, 1 ; posune pozici znaku dopredu
    sub r13, 1 ; snizi pocet mezer, ktere se maji pridat
    jmp mezery

output:
    cmp rcx, 0 ; zbyvajici pocet znaku 
    je prida_mezery ; která přidá mezery za řetězec
    mov al, [rsi] ; uloží znak z inputu do al
    mov [rdi], al
    add rsi, 1 ; přesune pointer na další znak v inputu
    add rdi, 1 ; přesune pointer na další znak v outputu
    sub rcx, 1 ; snizi pocet znaků
    jmp output

prida_mezery:
    cmp rbx, 2 ; prave zarovnani, mezery na konci nejsou potreba
    je done_align
    cmp rdx, 0 ;kolik ještě chubí mezer
    je done_align
    mov byte [rdi], 32 ; vloz mezeru
    add rdi, 1 ; posune ve stringu
    sub rdx, 1 ; odstrani mezeru
    jmp prida_mezery 

done_align:
    mov byte [rdi], 0 ; konec stringu
    ret



; section .bss
; input_buffer:
;     resb BUFFER_SIZE

; typeset:
;     mov rbp, rsp ; rbp zásobník
;     mov rcx, rdi ; délka načtených dat

; dalsi_radek:
;     mov r12, rsi

; zpracuj_radek:
;     cmp byte [rsi], 10 ; porovnej s '\n'
;     je formatuj
;     add rsi, 1
;     sub rcx, 1 ; snížení počtu zbylých znaků
;     jnz zpracuj_radek

; formatuj:
;     mov rdi, r12 ; předej začátek řádku jako první argument
;     call format_str ; Zavolá funkci format_str
;     mov rdi, r12 ; předej začátek řádku jako první argument
;     mov rsi, rdx ; předej velikost jako druhý argument
;     mov rdx, rcx ; předej zarovnání jako třetí argument
;     call align_str ; Zavolá funkci align_str

;     ; vypočítá délku řádku na print
;     mov r14, rsi ; uloži pointer
;     sub r14, r12 ; odečti začátek řádku,to dává délku řádku

;     ; výpis řádku
;     mov rax, SYS_WRITE ; sys_write
;     mov rdi, STDOUT ; stdout
;     mov rsi, r12  ; začátek řádku
;     mov rdx, r14  ; délka řádku
;     syscall

;     ; posun na další řádek
;     add r12, 1 ; byl dosažen konec vstupu?
;     cmp byte [r12], 0
;     je done_typeset
;     mov rsi, r12 ; Jinak zpracuje další řádek
;     jmp dalsi_radek

; done_typeset:
;     ret