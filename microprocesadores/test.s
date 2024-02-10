.data
vax1:   .word   31
vax2:   .word   43
vax3:   .word   0x1234

.text
.global main

main:   ldr x1, puntero_vax1
        ldr x1, [x1]
        ldr x2, puntero_vax2
        ldr x2, [x2]
        ldr x3, puntero_vax3
        add x0, x1, x2
        str x0, [x3]
        ret

puntero_var1: .word var1
puntero_var2: .word var2
puntero_var3: .word var3

