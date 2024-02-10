# Axiomas de probabilidad

Sea S un espacio muestral, una función P del conjunto de partes de S en
R se llamará función de probabilidad si satisface los siguientes
axiomas:

1.  Si $E \in S$ entonces $P(E) \geq 0$
2.  $P(S) = 1$
3.  Si $A \subset S$, $B \subset S$ y $A \cap B = \emptyset$ entonces
    $P(A \cup B) = P(A) + P(B)$

## Propiedades

1.  $P(\emptyset) = 0$
2.  $P(\bar{A}) = 1 - P(A)$
3.  $A \subset S$ entonces $P(A) \leq 1$

------------------------------------------------------------------------

Sean los eventos $A$ y $B$, son mutuamente excluyentes, si y solo si no
tienen elementos en común, es decir si $A \cap B = \emptyset$.

### Observación

Si $A \cap B = \emptyset$ $\implies$ $A$ y $B$ no mutuamente excluyentes
$\implies$ $P(A \cup B) = P(A) + P(B)$

Si $A \cap B \neq \emptyset$ $\implies$ $A$ y $B$ no mutuamente
excluyentes $\implies$ $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

### Complemento del evento

Notación: $A$ $\rightarrow$ $\bar{A}, A', A^c$

Definición: Son todos los elementos que pertenecen al espacio muestral, pero
no pertenecen al evento A.

$P(S) = 1 \implies P(A \cup \bar{A}) = P(A) + P(\bar{A}) = 1$

### Probabilidad condicional

$$P(A / B) = \frac{P(A \cap B)}{P(B)} \text{ con } P(B) \ne 0$$ 

$P(A / B)$ es la probabilidad de que ocurra el evento A, dado que ya
ocurrió el evento B.

### Regla de la multiplicación

$$P(A \cap B) = P(A / B) \cdot P(B) = P(B / A) \cdot P(A)$$

### Eventos independientes

$A$ y $B$ eventos independientes si y solo si la ocurrencia de uno
no afecta la ocurrencia del otro.

$P(A \cap B) = P(A) \cdot P(B)$

$P(A / B) = P(A)$

$P(B / A) = P(B)$
