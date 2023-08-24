# Notas del capítulo 5, sucesiones, inducción matemática y recurrencia.

# Sucesión

> DEFINICIÓN: Una sucesión es una función cuyo dominio es ya sean todos
> los naturales entre dos naturales dados o todos los naturales mayores
> o iguales a un natural dado.

> Definición de la profe: Es una función que tiene por dominio el
> conjunto de los naturales.

#### Y así sucesivamente

$$
2, 4, 8, 16, 32, 64, 128 \ldots \longrightarrow A_k = 2^k
$$

$a_k$ se lee "a subíndice k"; cada elemento se suyo se denomina término.

#### Notación de sucesión

-   Notación hasta n: $a_m, a_{m + 1}, a_{m + 2}, \ldots, a_n,$.

-   Notación infinita: $a_m, a_{m + 1}, a_{m + 2}, \ldots$

Una *fórmula explícita* o *fórmula general* para una sucesión es una
regla que muestra cómo los valores de $a_k$ dependen de $k$, por ejemplo
$a_k = 2^k$.

### Valores

-   Las sucesiones infinitas pueden tener valores finitos;
    $c_j = (-1)^j \text{ para todo entero } j \ge 0$.

-   Dos fórmulas diferentes pueden dar a sucesiones con los mismos
    términos:

$$
    a_k = \frac{k}{k + 1} \text{ para todo entero } k \ge 1,
$$

$$
    b_i = \frac{i - 1}{i} \text{ para todo entero } i \ge 2.
$$

### Ejemplo de sucesión a fórmula (5.1.3)

$$
1, -\frac{1}{4}, \frac{1}{9}, -\frac{1}{16}, \frac{1}{25}, -\frac{1}{36} \ldots
\rightarrow a_k = \frac{\pm1}{k^2}
\rightarrow a_k = \frac{(-1)^{k+1}}{k^2} \text{ para todo entero } k \ge 1.
$$

Alternativamente, también puede resolverse a
$\rightarrow a_k = \frac{(-1)^k}{(k + 1)^2} \text{ para todo entero } k \ge 0.$

# Notación de suma

> DEFINICIÓN: Si $m$ y $n$ son números naturales y $m \le n$, el símbolo
>
> $$\sum_{k=m}^{n} a_k$$
>
> Se lee como la suma desde $k$ igual a $m$ a $n$ de $a$ subíndice $k$,
> es la suma detodos los términos de
> $a_m, a_{m + 1}, a_{m + 2}, \ldots a_n$. Decimos que
> $a_m, a_{m + 1}, a_{m + 2}, \ldots a_n$ es la forma desarollada de la
> suma y se escribe como
>
> $$\sum_{k=m}^{n} a_k = a_m, a_{m + 1}, a_{m + 2}, \ldots a_n.$$
>
> LLamamos a $k$ al *índice* de la suma, a m al *límite inferior* de la
> suma y a $n$ al *límite superior* de la suma.

### Definición recursiva

> Una definición matemática más precisa de la suma, llamada una
> definición recursiva, es la siguiente: Si m es cualquier entero,
> entonces
>
> $$
> \sum_{k=m}^{m} a_k = a_m
> \text{ y } \sum_{k=m}^{n} a_k =
> \sum_{k=m}^{n - 1} a_k + a_n
> \text{ para todo entero } n \gt m.
> $$
>
> Cuando se resuelven problemas, con frecuencia es útil reescribir una
> suma usando la forma recursiva de la definición ya sea separando el
> término final de una suma o agregando un término final a una suma.

# Notación de producto

> DEFINICIÓN: Si $m$ y $n$ son enteros y $m \le n$, el símbolo
>
> $$\prod_{k=m}^{n}$$
>
> se lee como la *forma de producto de $k$ es igual a $m$ a $n$ de $a$
> subíndice $k$*, es el producto de todos los términos,
> $a_m, a_{m + 1}, a_{m + 2}, \ldots, a_n$. Se escribe
> $$ \prod_{k=m}^{n} a_k = a_m, a_{m + 1}, a_{m + 2}, \ldots, a_n.$$

### Propiedades

#### 1

$$ \sum_{k=m}^{n} a_k + \sum_{k=m}^{n} b_k = \sum_{k=m}^{n} (a_k + b_k) $$

#### 2

$$ c \cdot \sum_{k=m}^{n} a_k = \sum_{k=m}^{n} c \cdot a_k $$

#### 3

$$ (\prod_{k=m}^{n} a_k) \cdot (\prod_{k=m}^{n} b_k) = \prod_{k=m}^{n} (a_k \cdot b_k) $$

#### 4

$$ \sum_{k=m}^{n} a_k + \sum_{k=n+1}^{p} a_k = \sum_{k=m}^{p} a_k $$

### Factorial

> DEFINICIÓN: Para cada entero postivo $n$, la cantidad *$n$ factorial*
> que se denota por $n!$, se define como el producto de todos los
> enteros de 1 a $n$.
>
> $$ n! = n \cdot (n - 1) \ldots 3 \cdot 2 \cdot 1. $$
>
> *Cero factorial*, que se denota por $0!$, se define como 1:
>
> $$ 0! = 1. $$

### Combinaciones

> DEFINICIÓN: Sean $n$ y $r$ enteros con $0 \le r \le n.$ El símbolo
>
> $$ 
> \left(
> \begin{array}{lcr}
> n \\
> r
> \end{array}
> \right)
> $$
>
> Se lee *"$n$ se seleccionan $r$"* y representa el número de
> subconjuntos de tamaño $r$ que se pueden elegir de un conjunto con $n$
> elementos.
>
> Fórmula:
>
> Para todo entero $n$ y $r$ con $0 \le r \le n$,
>
> $$
> \left(
> \begin{array}{l}
> n \\
> r
> \end{array}
> \right)
> = \frac{n!}{r!(n - r)!}
> $$

# No imprimir

### Ejemplos

------------------------------------------------------------------------

$$ \frac{8 \cdot 7!}{7!} = 8 $$

*Los factoriales se cancelan*

------------------------------------------------------------------------

### Suma telescópica

$$
\sum_{k=1}^{n} \frac{1}{k(k+1)} \rightarrow
\sum_{k=1}^{n} \frac{1}{k} - \frac{1}{k+1} =
\frac{1}{1} - \frac{1}{2} +
\frac{1}{2} - \frac{1}{3} +
\frac{1}{3} - \frac{1}{4} +
\ldots
\frac{1}{n} - \frac{1}{n + 1}
$$

Cancelando se llega a:

$$
\sum_{k=1}^{n} \frac{1}{k} - \frac{1}{k+1} = \frac{1}{1} - \frac{1}{n+1}
$$

# Ejercicios

## Sucesiones

Escriba los cuatro primeros términos de las sucesiones definidas:

1.  $a_k = \frac{k}{10 + k}, \text{ para todo entero } k \ge 1.$

$$
a_1 = \frac{1}{11}, a_2 = \frac{2}{12}, a_3 = \frac{3}{13}, a_4 = \frac{4}{14}
$$

4.  $d_m = 1 + (\frac{1}{2})^m, \text{ para todo entero } m \ge 0$

$$
d_0 = 1, d_1 = 1 + \frac{1}{2}, d_2 = 1 + \frac{1}{4}, d_3 = 1 + \frac{1}{8}
$$

7.  Sea $a_k = 2k + 1$ y $b_k = (k - 1)^3 + k + 2$ para todo entero
    $k \ge 0$. Demuestre que los tres primeros términos en estas
    sucesiones son idénticos, pero que difieren en sus primeros cuatro
    términos.

$$
    a_0 = 2 \cdot 0 + 1 = 1, \\
    a_1 = 2 \cdot 1 + 1 = 3, \\
    a_2 = 2 \cdot 2 + 1 = 5, \\
    a_3 = 2 \cdot 3 + 1 = 9
$$

$$
\begin{align}
    b_0 &= (0 - 1) ^ 3 + 0 + 2 = -1 + 2 = 1, \\
    b_1 &= (1 - 1) ^ 3 + 1 + 2 = 1 + 2 = 3, \\
    b_2 &= (2 - 1) ^ 3 + 2 + 2 = 1 + 2 + 2 = 5, \\
    b_3 &= (4 - 1) ^ 3 + 4 + 2 = 27 + 4 + 2 = 33
\end{align}
$$

## 5.1

Determine las fórmulas explícitas para las sucesiones de la forma
$a_1, a_2, a_3, \ldots$ con los términos iniciales que se dan en los
siguientes ejercicios:

Definiciones globales:

> $$
> p(x) =
> \begin{cases}
> 1 \iff \lfloor \frac{x}{2} \rfloor \cdot 2 = x \\
> 0 \iff \lfloor \frac{x}{2} \rfloor \cdot 2 \ne x
> \end{cases}
> \forall x \in \mathbb{Z}
> $$

> $$
> r(x) =
> \begin{cases}
> x \iff p(x) = 1 \\
> r(x - 1) \iff p(x) = 0
> \end{cases}
> \forall x \in \mathbb{Z}
> $$

### 10

Sucesión:

$$ -1, 1, -1, 1, -1, 1 $$

Fórmula general sucesión:

$$ a_k = (-1)^k, \text{ para todo entero } k \ge 1 $$

Fórmula general sumatoria:

$$ \sum_{k=0}^{k=n} (-1)^k = -p(n-1) $$

### 11

Sucesión:

$$ 0, 1, -2, 3, -4, 5 $$

Fórmula general sucesión:

$$ a_k = (-1)^{k-1} \cdot k, \forall k \in \mathbb{Z} \ge 0 $$

Fórmula general sumatoria:

$$
\sum_{k=0}^{k=n} (-1)^{k-1} \cdot k =
(-1)^{n-1} \cdot \lceil \frac{n}{2} \rceil
$$

### 12

Sucesión:

$$ \frac{1}{4}, \frac{2}{9}, \frac{3}{16}, \frac{4}{25}, \frac{5}{36}, \frac{6}{49} $$

Fórmula general sucesión:

$$ a_k = \frac{k}{(k + 1)^2} \forall k \in \mathbb{N} \ge 1$$

Fórmula general sumatoria:

$$
\sum_{k=1}^{k=n} \frac{k}{(k+1)^2}=
$$

### 15

Sucesión:

$$0, -\frac{1}{2}, \frac{2}{3}, -\frac{3}{4}, \frac{4}{5}, -\frac{5}{6}, \frac{6}{7}$$

Fórmula general sucesión:

$$ a_k = (-1)^k \cdot \frac{k}{k + 1}, \text{ para todo entero } k \ge 0 $$

Fórmula general sumatoria:

$$ \sum_{k=0}^{k=n} (-1)^k \cdot \frac{k}{k + 1} = \frac{}{(n + 1)!} $$

### 16

Sucesión:

$$3, 6, 12, 24, 48, 96$$

Fórmula:

$$ a_k = 3 \cdot 2^k, \text{ para todo entero } k \ge 0 $$

Fórmula general sumatoria:

$$ \sum_{k=0}^{k=n} 3 \cdot 2^k = 3 \cdot (2^{n + 1} - 1) $$
