global obvod_o
global obsah_o
global obsah_ctverce
global obvod_trojuhelnika
global obvod_trojuhelnika2
global obsah_trojuhelnika2
global obsah_trojuhelnika3
global objem_krychle
global avg

section .text

obvod_o:
    mov eax, edi
    add eax, esi
    add eax, eax
    ret

obsah_o:
    mov eax, edi
    add eax, esi
    shl eax, 1
    ret

obsah_ctverce:
    mov eax, edi
    imul eax, eax
    ret

obvod_trojuhelnika:
    mov eax, edi
    add eax, esi
    add eax, edx
    ret

obvod_trojuhelnika2:
    mov eax, edi
    add eax, edi
    add eax, edi
    ret

obsah_trojuhelnika2:
    mov eax, edi
    imul eax, esi
    shr eax, 1
    ret

obsah_trojuhelnika3:
    mov eax, edi
    imul eax, esi
    shr eax, 1
    ret

objem_krychle:
    mov eax, edi
    imul eax, edi
    ret

avg:
    ; nacte prvni cislo
    mov eax, edi

    ; secte cisla
    add eax, esi
    add eax, edx

    ; deleni souctu 3
    mov ebx, 3
    xor edx, edx
    div ebx

    ; vrati vysledek
    ret