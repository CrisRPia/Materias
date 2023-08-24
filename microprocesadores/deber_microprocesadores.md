# ¿Qué tipos de interrupciones de CPU hay?

> Usé [Phind](https://www.phind.com/).

Las interrupciones de CPU son señales enviadas al procesador para
indicar que un evento necesita atención inmediata. Son una parte
fundamental de la arquitectura moderna de computadoras y vienen en
varios tipos, cada uno sirviendo diferentes propósitos.

Algunos tipos comunes de interrupciones de CPU incluyen:

1.  Interrupciones de Hardware: Estas son señales enviadas por
    dispositivos de hardware (como un mouse, teclado o adaptador de red)
    a la CPU, indicando que ocurrió un evento que necesita atención
    inmediata. Las interrupciones de hardware se utilizan comúnmente
    para indicar cambios de estado electrónicos o físicos que requieren
    atención sensible al tiempo. Por ejemplo, cuando mueves tu mouse,
    envía una señal de interrupción a la CPU para actualizar la posición
    del cursor en la pantalla. De manera similar, un adaptador de red
    podría enviar una interrupción a la CPU cuando recibe un paquete de
    datos, lo que provoca que la CPU procese los datos recibidos.

2.  Interrupciones de Software: Estas son interrupciones generadas por
    el propio procesador al ejecutar ciertas instrucciones o cuando se
    cumplen ciertas condiciones. Las interrupciones de software se
    utilizan a menudo para solicitar servicios del sistema operativo,
    interactuar con controladores de dispositivos o manejar errores de
    ejecución de programas. Por ejemplo, una aplicación de software
    podría emitir una interrupción de software para solicitar al sistema
    operativo que realice una tarea como leer de un archivo o enviar
    datos a través de una red.

3.  Interrupciones No Enmascarables (NMI): Estas son interrupciones que
    no pueden ser ignoradas por la CPU. Se utilizan típicamente en
    situaciones que requieren atención inmediata, como errores de
    hardware o problemas críticos del sistema.

4.  Interrupciones del Sistema: Las Interrupciones del Sistema es un
    proceso de Windows y representa las interrupciones de hardware en tu
    computadora. Un alto uso de CPU generalmente significa que una pieza
    de hardware o el controlador asociado con ella se está comportando
    mal.

5.  Solicitudes de Interrupción (IRQ): Estas son señales de hardware
    enviadas a la CPU que indican que un dispositivo conectado necesita
    su atención. Cada dispositivo conectado a la computadora se le
    asigna un número de IRQ único.

6.  Excepciones: Estas son un tipo de interrupción que ocurre en
    respuesta a una situación particular, como un error de división por
    cero, una instrucción inválida o un fallo de página. Las excepciones
    pueden ser categorizadas como faltas, trampas y abortos.

Cuando ocurre una interrupción, el procesador suspenderá sus actividades
actuales, guardará su estado y ejecutará una función llamada manejador
de interrupciones (o una rutina de servicio de interrupción, ISR) para
lidiar con el evento. Después de que el manejador de interrupciones
termina, la CPU reanuda sus actividades normales.

## Referencias

1. Wikipedia. (n.d.). Interrupt. Retrieved from
<https://en.wikipedia.org/wiki/Interrupt> CPUsage. (n.d.). System
2. Interrupts. Retrieved from
<https://www.cpusage.com/blog/system-interrupts/> Witscad. (n.d.). CPU
3. Interrupts and Interrupt Handling. Retrieved from
<https://witscad.com/course/computer-architecture/chapter/cpu-interrupts-and-interrupt-handling>
