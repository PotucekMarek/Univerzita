section .text

global format_str
global align_str

format_str:
    mov al, [rsi] ; do al se da character z rsi
    add rsi, 1
    cmp al, 0  ; jestliže je '\0' konci
    jz done
    cmp al, 42  ; jestli je znak * skoc do oznac_hvezdu
    je oznac_hvezdu
    cmp al, 95 ; jestli je znak _ skoc do oznac_podtrzitko
    je oznac_podtrzitko
    jmp zpracuj

oznac_hvezdu:
    cmp rcx, 0  ; to urci 1. nebo 2. *
    jz prvni_hvezda
    mov rcx, 0
    jmp buffer

prvni_hvezda: ; ulozi si, že jsme stale v *
    mov rcx, 1
    jmp buffer

oznac_podtrzitko:
    cmp rdx, 0 ; to urci 1. nebo 2. _
    jz prvni_podtrzitko
    mov rdx, 0
    jmp buffer

prvni_podtrzitko: ; ulozi si, že jsme stale v _
    mov rdx, 1
    jmp buffer

zpracuj:
    cmp rcx, 0 ; jestli je 1. hvezda, konvertuje
    je konvert_hvezdy
    cmp rdx, 0
    je konvert_podtrzitka ; podiva se na podtrzitko
    jmp buffer

konvert_hvezdy:
    cmp al, 97 ; 'a'
    jb buffer
    cmp al, 122 ; 'z'
    ja buffer
    sub al, 32 ; mezi 97-122 prevede na velke pismeno

konvert_podtrzitka:
    cmp al, 32 ; pokud je mezera, zmen na _
    jne buffer
    mov al, 95

buffer:
    mov [rdi], al
    add rdi, 1
    jmp format_str ; skoč na začatek

done:
    mov [rdi], al
    ret


; asi mi kolidují registry, jaké použít?
align_str:
    ; rdx size, rdi output, rsi input (není to lepší uložit do r12-r15? pak se podívej)
    mov rbx, rcx; tmp (tady možná použít rbx)
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
    shr rdx, 1;je potřeba upravit rdx
    mov r13, rdx ; kolik je mezer, ktere se pridaji pred retezec
    jmp mezery

na_pravo:
    mov r13, rdx  ; kolik je mezer, ktere se pridaji pred retezec
    jmp mezery 

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