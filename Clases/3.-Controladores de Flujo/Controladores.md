# Controladores de flujo


### ¿Qué es el flujo?

Veremos cómo controlar el flujo con Python, pero antes de eso, ¿Qué es el flujo?. El flujo es una forma de entender la sucesión de las instrucciones de un programa, estas instrucciones se ejecutan una después de otras de forma ordenada y suelen tener el objetivo final de manipular información. Sin embargo, para manipular datos no es suficiente con realizar cálculos o resolver expresiones, necesitamos que de alguna forma nuestro programa pueda elegir, que sepa cómo actuar en función de determinadas situaciones, o incluso repetir una tarea si es necesario.
Para estas situaciones, existen las sentencias de control de flujo.

### Sentencias de control

Se dividen en dos tipos, las de control condicional y las de control iterativo. (A las siguientes imágenes se le denomina diagrama de flujo)
Nos centraremos en las sentencias de control condicional.

### Diagramas de flujo

Expresan nuestros algoritmos en forma de diagrama mediante una representación gráfica basada en figuras geométricas que varían según la estructura de código. Una app recomendada que se suele utilizar es Diagrams.

#### Condicional

En la vida diaria, actuamos de acuerdo a la evaluación de condiciones, de manera mucho más frecuente de lo que en realidad creemos: si el semáforo está en verde, cruzar la calle. Si no, esperar a que el semáforo se ponga en verde.

A veces, también evaluamos más de una condición para ejecutar una determinada acción: si llega la factura de la luz y tengo dinero, pagar la factura. Las sentencias de control condicionales, son aquellas que nos permiten evaluar si una o más condiciones se cumplen, para decir qué acción vamos a ejecutar. La evaluación de condiciones, solo puede arrojar 1 de 2 resultados: True o False (verdadero o falso).

Para describir la evaluación a realizar sobre una condición, se utilizan los operadores relacionales (==, !=, >, <, etc.). Y, para evaluar más de una condición simultáneamente se utilizan los operadores lógicos (not, and, or).
Las sentencias de control de flujo condicionales se definen mediante el uso de tres palabras claves reservadas:

if (si)
elif (si no, si)
else (si no)


1. Sentencia If

Dentro de las sentencias condicionales el if (si) posiblemente sea la más famosa y utilizada en la programación, esto debido a que nos permite controlar el flujo del programa y dividir la ejecución en diferentes caminos.
Al utilizar esta palabra reservada if le estamos indicando a Python que queremos ejecutar una porción de código, o bloque de código, solo si se se cumple una determinada condición, es decir, si el resultado es True.

Primero definimos una variable edad y le asignamos un valor entero 30. Después, a través del condicional, le decimos que queremos imprimir “Es un adulto” en pantalla, solo si se cumple la condición de que edad sea mayor o igual a 18.
Veamos el siguiente ejemplo:

edad =  30
if edad >= 18:
    print('Es un adulto')
if True:
    print('Se cumple la condición')



2. Indentación

Python se basa en la sangría (espacio en blanco al comienzo de una línea) para definir el alcance en el código. Otros lenguajes de programación a menudo usan corchetes para este propósito.

El siguiente código nos arrojará un error:

a = 25
b = 50
if b > a:
print("b es más grande que a")

Puedes probarlo para verificarlo.


Recordemos que Python admite las condiciones lógicas habituales de las matemáticas:

Es igual a : a == b
No es igual a: a != b
Menos que: a < b
Menor o igual que: a <= b
Mayor que: a > b
Mayor o igual que: a >= b


También podemos apoyarnos del uso de operadores lógicos como ser: AND, OR, NOT.




Ejemplo con AND: 

a = 195
b = 30
c = 400
if a > b and c > a:
  print(“Ambas condiciones son verdaderas")


Ejemplo con OR: 
a = 195
b = 50
c = 500
if a > b or a > c:
  print(“Al menos una de las condiciones es verdadera")


Ejemplo con NOT: 
x = 10
if not x > 15:
    print("False")


If en una sola línea – Ejemplo 1: 
a = 150
b = 35
if a > b: print(“a es mayor que b")

If en una sola línea – Ejemplo 2:
a = 5
b = 150
print("A") if a > b else print("B")


If en una sola línea – Ejemplo 3:

a = 150
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#### Else

Sentencia Else

Dentro de las sentencias condicionales el else (si no) es una especie de “hermano” de if el cual se puede encadenar al final de un bloque de código if para comprobar los casos contrarios, es decir los False.

Al utilizar esta palabra reservada else le estamos indicando a Python que queremos ejecutar una porción de código, o bloque de código, solo si no se cumple ninguna de las condiciones antes dichas, es decir, si el resultado es False siempre.

Primero definimos una variable número y le asignamos un valor entero 24. 
Después, a través del condicional, le preguntamos si el número es mayor a 36, si es así, queremos imprimir “El número es más grande” en pantalla, de lo contrario queremos que imprima “El número es más chico”.
2
1

Veamos el siguiente ejemplo:

numero =  24
if numero > 36:
    print("El número es grande")
else:
    print("El número es chico")
SENTENCIA ELSE

Múltiples If

Veamos un ejemplo de cómo podemos trabajar con múltiples ifs anidados: 

Ejemplo 1:

x = 25
if x > 10:
  print("por encima de diez,")
  if x > 20:
    print("y también por encima de 20!")
  else:
    print("pero no por encima de 20")

Ejemplo 2:

x = 15
if x > 10:
  print("por encima de diez,")
  if x > 20:
    print("y también por encima de 20!")
  else:
    print("pero no por encima de 20")
Profesor/a: explicar codeando en vivo los ejemplos y explicar qué ha pasado al utilizar con múltiples ifs anidados. 

#### Elif

Sentencia Elif
La última sentencia condicional que podemos encontrar es el elif (si no, si), también podríamos decir que es un hermano de if, ya que se utiliza en continuación al if para poder encadenar muchísimas más comprobaciones.


Al utilizar esta palabra reservada elif le estamos indicando a Python que queremos ejecutar una porción de código, o bloque de código, solo si la condición anterior no se cumple, es decir, si el resultado del if o algún elif fue False.

SENTENCIA ELIF

a = 2 + 3
if a == 4: 
   print ("A es igual a cuatro")
elif a == 5:
   print ("A es igual a cinco")
elif a == 6:
   print ("A es igual a seis")
else:
   print ("No se cumple la condición")

Como podemos observar, la primera condición valida si A es igual a 4, como esto no es verdadero, se evalúa la siguiente condición, si A es igual a 5, si no A es igual a 6?. Finalmente, se define un bloque else por default que se ejecutará cuando ninguna de las condiciones anteriores sea verdadera.

Pregunta! ¿Cuál sería el resultado de este ejemplo?
El resultado es: "A es igual a cinco"

comando =  "SALIR"
if comando == "ENTRAR":
    print("Bienvenido al sistema.")
elif comando == "SALUDO":
    print("Hola! ¿Cómo estás?")
elif comando == "SALIR":
    print("Saliendo del sistema.")
else:
    print("No se reconoce el comando.")



Básicamente, nos sirve para poder darle múltiples opciones al programa.
¿Para qué sirve la sentencia Elif?

Cuando se tiene varios if’s se ven las múltiples condiciones y si todo está bien, nos mostrará el resultado de cada if.
Sin embargo, en el caso de múltiples elif, comprueba las condiciones de arriba a abajo hasta que se cumpla una de ellas, y de ser así, las demás no se comprueban.


Sentencias iterativas
Repetir
Veremos cómo controlar el flujo con Python, pero antes de eso, ¿Qué es el flujo?. El flujo es una forma de entender la sucesión de las instrucciones de un programa, estas instrucciones se ejecutan una después de otras de forma ordenada y suelen tener el objetivo final de manipular información.

Iterar
En matemática, se refiere al proceso de iteración de una función, es decir, aplicando la función repetidamente, usando la salida de una iteración como la entrada a la siguiente. En programación, Iteración es la repetición de un segmento de código dentro de un programa de computadora. Puede usarse tanto como un término genérico (como sinónimo de repetición) como para describir una forma específica de repetición.
Tenemos una base de datos enorme y queremos encontrar un dato en especial para consultar. Como no existe una forma mágica para encontrar el dato directamente, el programa deberá recorrer los datos uno a uno y compararlos hasta dar con el que buscamos iterando o repitiendo el mismo proceso desde el inicio comparando a ver si es el que queremos o no, así hasta que encuentre el que queremos.
Existen algoritmos que permiten ahorrarnos tiempo e iteraciones, pero en esencia sigue recorriendo uno a uno, la diferencia es que nosotros tardaríamos muchas horas, y el programa unos segundos. 

¡Así que vamos a aprovecharnos de esto! 

While  (no sabes la cantidad)

Vamos a comenzar con la sentencia iterativa más básica While (mientras). Se basa en repetir un bloque de código a partir de evaluar una condición lógica, siempre que esta sea True (al igual que la sentencia if). Nosotros como programadores debemos decidir el momento en que la condición cambie a False para hacer que el While finalice su ejecución y así salir de la iteración, de lo contrario estaríamos frente a un bucle infinito.

Sentencia While

Flujo de ejecución
Más formalmente, el flujo de ejecución de una sentencia while es el siguiente:

1. Evalúa la condición, devolviendo False o True.


2. Si la condición es False, se sale de la sentencia While y continúa la ejecución con la siguiente sentencia.


3. Si la condición es True, ejecuta cada una de las sentencias en el bloque de código y regresa al paso 1.

Bucle
Este tipo de flujo se llama bucle porque el tercer paso del bucle vuelve arriba.  Si la condición es falsa la primera vez que se pasa el bucle, las sentencias del interior del bucle no se ejecutan nunca.
Ejemplo
Analicemos qué pasó: 

num = 5
while num > 0:
    print(f'{num}')
    num -= 1
    print('Terminó el conteo!')

1. Declaramos una variable num y le asignamos el valor int 5.
2. Usamos la sentencia while para indicar que mientras que num sea mayor a 0 entremos al bloque de código.
3. Al evaluar num contra 0 nos indica que es True.
4. Ingresamos al bloque de código, imprimimos num y le restamos 1 a num
5. Volvemos a repetir desde el paso 2 hasta que num deje de ser mayor a 0
6. Cuando la operación relacional de False saldremos del bucle 
7. Imprimimos por pantalla Terminó el conteo! 

8. Termina nuestro programa
Más ejemplos
n = 0
while n <= 5:
    n += 1
print('N vale ', n)

¿Y un bucle infinito?

 while True:
print(“Esto es un bucle infinito!!!!!”)

Para escapar un bucle infinito generalmente se usa ctrl + c 😎. También podemos usar la opción de Restart Kernel! En Jupyter Notebook

While - Else
Sentencia While-else
Veamos un ejemplo:

chance  = 1
while chance <= 3:
  txt = input("Escribe SI: ")
  if txt == "SI":
     print("Ok, lo conseguiste en el intento", chance)
     break
  chance += 1
else:
  print("Has agotado tus tres intentos")
Este else sirve para ejecutar un bloque de código cuando el bucle while tenga una condición False o haya terminado y no haya sido forzado a salir mediante un break.

Qué ha pasado?

1. Declaramos una variable chance y le asignamos el valor int 1.
2. Usamos la sentencia while para indicar que mientras que chance sea menor a 3 entremos al bloque de código.
3. Le pedimos al usuario que ingrese una palabra con input
Sentencia While-else
4. Si la palabra es “SI” ingresa al condicional if
5. Si ingresa, imprime que lo consiguió en el intento tal y rompe el bucle con break
6. Si la condicional es False vamos a sumar uno a las chances y repetir desde el paso 2
7. Si chance es mayor a 3, entramos en el else  e imprimimos
¡Solicitud de números al usuario!

Instrucciones

Bucles en Python
Usar bucles en Python nos permite automatizar y repetir tareas de manera eficiente. Sin embargo, a veces, es posible que un factor externo influya en la forma en que se ejecuta su programa. 

Continue
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle. Es decir, la iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior del bucle. Debe poner la instrucción continue dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una sentencia if condicional.

Veamos un ejemplo:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


Ejecuta el código para analizar que fue lo que paso!

Pass

Cuando se activa una condición externa, la instrucción pass permite manejar la condición sin que el bucle se vea afectado de ninguna manera; todo el código continuará leyéndose a menos que se produzca la instrucción break u otra instrucción. Debes poner la instrucción pass dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una sentencia if condicional.

#Ejemplo 1
n = 0
while n < 10:
    n += 1
    if n == 2:
        pass
    print('n vale' , n)

#Ejemplo 2
n = 0
while n < 10:
    n += 1
    if n == 2:
        pass
        print('n vale' , n)

Ejecuta el código para analizar las diferencias ☺

For (repetir pero sabiendo la cantidad)

Sentencia For
Ahora seguiremos con la sentencia iterativa que podríamos decir es la más usada For (para). Se utiliza para recorrer los elementos de un objeto iterable (lista, tupla…) y ejecutar un bloque de código, o sea, tiene un número predeterminado de veces que itera. 
En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cual se pueden aplicar una serie de operaciones.

lista = [1,2,3,4,5]
for valor in lista:
    print('Soy un item de la lista y valgo', valor)



Ejemplo gráfico

Valor simplemente es una copia local, no afecta fuera del bucle a menos que se devuelva el valor.

lista = [0,1,2,3,4,5,6,7,8,9,10]
for num in lista:
    print('Soy un valor de la lista y valgo', num)
    num *= 5
    print('Soy un valor de la lista y ahora valgo', num)

indice = 0
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numeros[indice] *= 5
    indice += 1
print(numeros)		




Enumerate

El primero de los dos indica la posición de un elemento perteneciente al objeto iterable, es decir, el índice.
El segundo, el elemento mismo.
2
1

La función incorporada enumerate(lista/tupla_de_valores) toma como argumento un objeto iterable y retorna otro cuyos elementos son tuplas de dos objetos:

👉 Esto se conoce como lectura secuencial de clave y valor, lo vamos a usar bastante en el futuro! La función incorporada enumerate(lista/tupla_de_valores) toma como argumento un objeto iterable y retorna otro cuyos elementos son tuplas de dos objetos:

Sentencia For
Si quisiéramos recorrer un string:

texto = 'Hola Mundo, estoy usando for en Python'
for letra in texto:
    print(letra)
    
texto2 = ''
for letra in texto:
    texto2 = letra * 2
print(texto2)
Profesor/a: mostrar codeando el ejemplo

Range
¿Qué es?
Como vimos, el for en Python necesita una colección de datos para poder utilizarlo, en otros lenguajes necesitamos solamente un número para indicar las iteraciones a cumplir. Para simular estos casos Python nos provee de una función denominada range() (rango) el cual representa una colección de números inmutables.
3
2
1

Constructores para crear objetos Range
range(fin): Crea una secuencia numérica que va desde 0 hasta fin - 1.
a. for numero in range(10)
range(inicio, fin): Crea una secuencia numérica que va desde inicio hasta fin - 1.
a. for numero in range(5, 10)
range(inicio, fin, [paso]): Crea una secuencia numérica que va desde inicio hasta fin - 1. Si además se indica el parámetro paso, la secuencia genera los números de paso en paso.
a. for numero in range(0, 20, 2)
>>> range(0,10)
Parece ser exactamente una lista que va de 0 a 10, pero range interpreta el inicio y fin en tiempo de ejecución y eso le da ventaja contra la lista.
Si tuviéramos una lista de 0 a 10000 estaría ocupando muchísimo espacio en memoria.
>>> range(0,10000)
Ahora, si hiciéramos range(0,10000), range interpreta esto en tiempo de ejecución, es decir cuando se ejecuta el 0 se crea el 0 cuando se ejecuta el 1 se crea el 1 y se elimina el 0 y así continuamente, y esto no ocupa memoria.

Instrucciones
Cuando esto sucede, es posible que prefiramos que nuestro programa cierre un bucle por completo, omita parte de un bucle antes de continuar o ignore ese factor externo.
Para hacer estas acciones Python nos brinda las instrucciones break, continue y pass.
Comencemos por uno de los más sencillos y más utilizados: break.
En Python, la instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una sentencia if condicional.





Ejemplo
Salimos del bucle cuando i es igual a 3

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

