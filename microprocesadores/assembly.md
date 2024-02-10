# Notas de assembly

Python:

``` python
var1 = 31
var2 = 43
var3 = 0x1234

r1 = var1
r2 = var2
r0 = r1+r2

var3 = r0

print("El valor de var1 es:", var1)
print("El valor de var2 es:", var2)
print("El valor de var3 es:", var3)
```

Assembly:

``` asm
.data
var1:   .word   31
var2:   .word   43
var3:   .word   0x1234

.text
.global main

main:   ldr r1, puntero_var1
        ldr r1, [r1]
        ldr r2, puntero_var2
        ldr r2, [r2]
        ldr r3, puntero_var3
        add r0, r1, r2
        str r0, [r3]
        bx lr

puntero_var1: .word var1
puntero_var2: .word var2
puntero_var3: .word var3
```

Assembly corregido para RPI4
``` asm
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
        bx lr

puntero_var1: .word var1
puntero_var2: .word var2
puntero_var3: .word var3
```
