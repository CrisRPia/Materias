# Microprocesadores

Microprocesador: Es un circuito electrónico que realiza operaciones
lógicas y aritméticas para ejecutar programas informáticos.

Está constituido por transistores que conforman circuitos lógicos
capaces de realizar operaciones básicas. Está conformado además
internamente por bloques fundamentales:

-   Unidad de control.
-   ALU (Unidad Aritmético Lógica)
-   Registros internos.
-   Buses internos.
-   Interrupciones.

### Proceso de funcionamiento

1.  El microprocesador, al iniciarse, como todos los sistemas
    secuenciales, se inicializará en una posición de memoria definida,
    desde donde empieza el proceso.
2.  El sistema lee el dato que hay en esa posición y lo envía a la
    unidad de control.
3.  La unidad de control decodifica la instrucción y la ejecuta dando
    señales adecuadas.
4.  Se incrementa el contador de programa.
5.  Se vuelve a repetir desde el punto 2 y así sucesivamente hasta que
    una señal exterior interrumpa el proceso.

### Unidad de control

Es el cerebro del microprocesador ya que genera todas las señales tanto
de control interno como externo.

Le llegan unos códigos que son decodificados y ejecutados. Son
instrucciones.

### Tipos de instrucciones

1.  La realización de una operación aritmetico-lógica.
2.  Cargar o leer datos.
3.  Saltos o interrupciones.

### Período y frecuencia

Siendo T período (intervalo entre pulsos del procesador) y f la
frecuencia (velocidad del procesador):

$$ T = \frac{1}{\text{f}} $$

## Sistemas analógicos y digitales.

### Electrónica Analógica:

Las señales eléctricas pueden tomar infinitos valores; la función es
como un sen(x), con cambios graduales. Se utilzan en audio; un micrófono
requiere una tasa de muestreo superior al doble de la frecuencia
objetivo al convertir de analógica a digital.

### Electrónica Digital:

Las señales eléctricas solo pueden tomar dos valores: 1 o 0, nivel alto
o nivel bajo.

### Sistemas de numeración:

$$ \text{Decimal: } 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. $$

$$ \text{Octal, } 0, 1, 2, 3, 4, 5, 6, 7. $$

$$ \text{Base cinco: } 0, 1, 2, 3, 4. $$

$$ \text{Binario: } 0, 1 $$

$$ \text{Hexadecimal: } 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F $$

#### Sistema binario

En electrónica digital solo pueden darse dos niveles o estados posibles,
por lo que debe aplicarse el sistema binario o sistema en base 2.

Si bien tiene solo dos dígitos o bits: 0 y 1, es posible representar
cualquier cantidad combinando adecuadamente dichos dígitos en grupos de
dos, tres, cuatro, etc.

$$ a_4 \cdot ^4 + a_3 \cdot ^3 + a_2 \cdot ^2 + a_1 \cdot ^1 + a_0 \cdot 2^0 $$

Ejemplo:

$$
10111_2 = 
    1 \cdot 2^4 + 
    0 \cdot 2^3 + 
    1 \cdot 2^2 + 
    1 \cdot 2^1 + 
    1 \cdot 2^0 =
        23_10
$$

> TODO: Esto quedó mal explicado, corregirlo luego. $$
> \frac{23}{2} = 11 \text{ (resto 1)}, 
> $$

$$
\frac{11}{2} = 5 \text{ (resto 1)},
$$

$$
\frac{5}{2} = 5 \text{ (resto 1)},
$$

$$
\frac{2}{2} = 1 \text{ (resto 0)},
$$

Leyendo el resultado de la división final y los restos de abajo a
arriba, se lee 10111, el valor original.

### BCD (Decimal codificado en binario)

COnsiste en transformar cada dígito digital en un grupo de h dígitos
binarios o cuarteto.

Por cada cifra decimal habrá un cuarteto BCD.

Ejemplo: $23_{10}$

$$ 2 \Leftrightarrow 0010 $$

$$ 3 \Leftrightarrow 0011 $$

### Sistema hexadecimal

Un número binario se puede representar por grupos de 4 dígitos
(cuartetos). Un cuarteto tiene 16 combinaciones posibles de ceros y
unos. Para simplificar la representación se recurre a un sistema de numeración
con base 16.

Hexadecimal: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E y F

<table class="card" style="width: fit-content;">
    <tr>
        <td align="center" colspan="1">
            Decimal
        </td>
        <td align="center" colspan="1">
            Hexadecimal
        </td>
        <td align="center" colspan="1">
            BCD
        </td>
        <td align="center" colspan="1">
            Binario
        </td>
    </tr>
    <tr>
        <td>
            <p> 0 </p>
            <p> 1 </p>
            <p> 2 </p>
            <p> 3 </p>
            <p> 4 </p>
            <p> 5 </p>
            <p> 6 </p>
            <p> 7 </p>
            <p> 8 </p>
            <p> 9 </p>
            <p> 10 </p>
            <p> 11 </p>
            <p> 12 </p>
            <p> 13 </p>
            <p> 14 </p>
            <p> 15 </p>
        </td>
        <td>
            <p> 0 </p>
            <p> 1 </p>
            <p> 2 </p>
            <p> 3 </p>
            <p> 4 </p>
            <p> 5 </p>
            <p> 6 </p>
            <p> 7 </p>
            <p> 8 </p>
            <p> 9 </p>
            <p> A </p>
            <p> B </p>
            <p> C </p>
            <p> D </p>
            <p> E </p>
            <p> F </p>
        </td>
        <td>
            <p> 0000 </p>
            <p> 0001 </p>
            <p> 0010 </p>
            <p> 0011 </p>
            <p> 0100 </p>
            <p> 0101 </p>
            <p> 0110 </p>
            <p> 0111 </p>
            <p> 1000 </p>
            <p> 1001 </p>
            <p> 0001 0000 </p>
            <p> 0001 0001 </p>
            <p> 0001 0010 </p>
            <p> 0001 0011 </p>
            <p> 0001 0100 </p>
            <p> 0001 0101 </p>
        </td>
        <td>
            <p> 0000 </p>
            <p> 0001 </p>
            <p> 0010 </p>
            <p> 0011 </p>
            <p> 0100 </p>
            <p> 0101 </p>
            <p> 0110 </p>
            <p> 0111 </p>
            <p> 1000 </p>
            <p> 1001 </p>
            <p> 1010 </p>
            <p> 1011 </p>
            <p> 1100 </p>
            <p> 1101 </p>
            <p> 1110 </p>
            <p> 1111 </p>
        </td>
    </tr>
</table>

<style>
    .card {
        width: fit-content;
    }
</style>

<table class="card" style="width: fit-content;">
    <tr>
        <td align="center" colspan="1">
            Elemento
        </td>
        <td align="center" colspan="1">
            Símbolo CEI
        </td>
        <td align="center" colspan="1">
            Símbolo MIL
        </td>
    </tr>
    <tr>
        <td>
         <p> Puerta NOT </p>
         <p> Puerta AND </p>
         <p> Puerta NAND </p>
         <p> Puerta OR </p>
         <p> Puerta NOR </p>
         <p> Puerta XOR </p>
        </td>
        <td>
        </td>
        <td>
        </td>
    </tr>
</table>

