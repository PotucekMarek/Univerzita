global uthread_internal_yield
global uthread_start_scheduler
global uthread_run
global uthread_mainthread_context 

; struktura obsahujici aktivni vlakno, predevsim jeho kontextu
extern uthread_active_tcb

; funkce, ktera se postara o zarazeni vlakna do odpovidajici struktu
extern uthread_switch

; akceptuje jeden argument, ktery udava, jestli pri prepnuti ma byt vlakno
; zarazeno mezi ostatni vlakna, nebo ma byt vlakno blokovano,
; tento argument se predava okamzite
uthread_internal_yield:
	; ulozi kontext aktualniho vlakna
	pop rax ; nacte navratovou adresu z/do vlakna

	mov rdx, [uthread_active_tcb]
	mov [rdx], rax
	mov [rdx + 8], rsp
	mov [rdx + 16], rbp
	mov [rdx + 24], rbx
	mov [rdx + 32], r12
	mov [rdx + 40], r13
	mov [rdx + 48], r14
	mov [rdx + 56], r15
	jmp uthread_switch

; zacne provadet vlakno ulozene v uthread_active_tcb
uthread_run:
	mov rdx, [uthread_active_tcb]

    	mov rsp, [rdx + 8]
	mov rbp, [rdx + 16]
	mov rbx, [rdx + 24]
	mov r12, [rdx + 32]
	mov r13, [rdx + 40]
	mov r14, [rdx + 48]
	mov r15, [rdx + 56]
	
	jmp [rdx]


; spusti planovani vlaken, navrat z funkce je proveden
; kdyz jiz nebezi zadne vlakno
uthread_start_scheduler:
	; ulozi kontext volajici funkce
	mov rdx, uthread_mainthread_context
	mov [rdx + 8], rsp
	mov [rdx + 16], rbp
	mov [rdx + 24], rbx
	mov [rdx + 32], r12
	mov [rdx + 40], r13
	mov [rdx + 48], r14
	mov [rdx + 56], r15

	; do uthread_mainthread_context->rip ulozi adresu kodu, ktery funkci ukonci
	mov qword [rdx], uthreads_complete

	; na zacatku neni aktivni zadne vlakno
	mov qword [uthread_active_tcb], 0

	; neblokujeme vlakno
	mov rdi, 0	
	jmp uthread_switch

uthreads_complete:
	ret

section .bss
uthread_mainthread_context:
	resq 8 ; pamet nutna pro ulozeni kontextu, s ostatnimi hodnotami nepracujeme 


