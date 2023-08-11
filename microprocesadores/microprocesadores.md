# Microprocesadores
Microprocesador: Es un circuito electrónico que realiza operaciones lógicas y
aritméticas para ejecutar programas informáticos.

Está constituido por transistores que conforman circuitos lógicos capaces de
realizar operaciones básicas. Está conformado además internamente por bloques
fundamentales: 

- Unidad de control.
- ALU (Unidad Aritmético Lógica)
- Registros internos.
- Buses internos.
- Interrupciones.

### Proceso de funcionamiento
1. El microprocesador, al iniciarse, como todos los sistemas secuenciales, se
inicializará en una posición de memoria definida, desde donde empieza el
proceso.
2. El sistema lee el dato que hay en esa posición y lo envía a la unidad de
control.
3. La unidad de control decodifica la instrucción y la ejecuta dando señales
adecuadas.
4. Se incrementa el contador de programa.
5. Se vuelve a repetir desde el punto 2 y así sucesivamente hasta que una señal
exterior interrumpa el proceso.

### Unidad de control
Es el cerebro del microprocesador ya que genera todas las señales tanto de
control interno como externo.

Le llegan unos códigos que son decodificados y ejecutados. Son instrucciones.

### Tipos de instrucciones
1. La realización de una operación aritmetico-lógica.
2. Cargar o leer datos.
3. Saltos o interrupciones.

### Período y frecuencia
Siendo T período (intervalo entre pulsos del procesador) y f la frecuencia (velocidad del procesador):
$$
T = \frac{1}{\text{f}}
$$
