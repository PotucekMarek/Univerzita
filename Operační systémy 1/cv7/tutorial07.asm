global _start

; deklarace konstant

SYS_WRITE equ 1 ; systemove volani pro zapis do souboru
SYS_EXIT equ 60 ; systemove volani pro ukonceni programu
STDOUT equ 1 ; deskriptor souboru standardniho vystupu

OUTPUT_SIZE    equ 105

section .text

;;;;;;;;;;;;;;;;;;;;;

; _start:
;     mov rax, SYS_WRITE ; vypsani retezce Hello World
;     mov rdi, STDOUT
;     mov rsi, str_hello
;     mov rdx, STR_HELLO_LEN
;     syscall
;     mov rax, SYS_EXIT ; ukonceni programu
;     mov rdi, 42
;     syscall
; ;
; ; (inicializovana) data programu
; ;
; section .data
; str_hello:
;     db "Hello World!", 10

;;;;;;;;;;;;;;;;;;;;

_start:
    mov rbx, buffer  ; row number
    mov rcx, 5

row_loop:
    mov rdx, 20 ; column number

column_loop:
    mov byte [rbx], '*'
    add, rbx, 1
    sub rdx, 1
    jnz column_loop

    mov byte [rbx], '\n'
    add rbx, 1

    sub rcx, 1
    jnz row_loop

    mov rax, SYS_WRITE
    mov rdi, STDOUT
    mov rsi, buffer
    mov rdx, OUTPUT_SIZE
    syscall

section .bss
buffer:
    resb OUTPUT_SIZE