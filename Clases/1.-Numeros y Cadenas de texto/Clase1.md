# Cadenas de texto y datos numericos.

## Numeros

#### Los números de Python están relacionados con los números matemáticos, pero están sujetos a las limitaciones de la representación numérica en las computadoras. Python distingue entre enteros, números de punto flotante y números complejos.

### Enteros
#### Los números enteros son aquellos que no tienen decimales, tanto positivos como negativos (además del cero). En Python se pueden representar mediante el tipo int (de integer, entero) o el tipo long (largo). La única diferencia es que el tipo long permite almacenar números más grandes.

### Float o decimal
#### Los números reales, son los que tienen decimales, en Python se expresan mediante el tipo float. Desde Python 2.4 cuenta con un nuevo tipo Decimal, para el caso de que se necesite representar fracciones de forma más precisa.

### Cadenas de texto
#### Las cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles.

### Variables
#### En algunos lenguajes de programación, las variables se pueden entender como "cajas" en las que se guardan los datos, pero en Python las variables son "etiquetas" que permiten hacer referencia a los datos (que se guardan en unas "cajas" llamadas objetos).

## Las variables en Python no guardan los datos, sino que son simples nombres para poder hacer referencia a esos objetos.  

## Los nombres de las variables pueden contener mayúsculas, pero ten en cuenta que Python distingue entre mayúsculas y minúsculas (en inglés se dice que Python es case-sensitive).

# INPUT
#### En Informática, la "entrada" o input de un programa son los datos que llegan al programa desde el exterior. Actualmente, el origen más habitual es el teclado.
#### Python tiene una función llamada input() la cual permite obtener texto escrito por teclado. Al llegar a la función, el programa se detiene esperando que se escriba algo y se pulse la tecla Intro.

# Metodos para manipular cadenas de texto

1. upper()
Saludo = ‘hola mundo’
Print(Saludos.upper())

2. lower()
Devuelve la cadena con todos sus caracteres a minúscula:
Saludo = ‘hola mundo’
Print(Saludos.lower())

3. capitalize()
Devuelve la cadena con su primer carácter en mayúscula:
Saludo = ‘hola mundo’
Print(Saludos. capitalize ())

4. title()
Devuelve la cadena con el primer carácter de cada palabra en mayúscula:
Saludo = ‘hola mundo’
Print(Saludos. title())
count()
Devuelve una cuenta de las veces que aparece una subcadena en la cadena:
Saludo = ‘hola mundo’
Print(Saludos.count (mundo))


5. isdigit()
Devuelve True si la cadena es todo números (False en caso contrario):
c = "100"
c.isdigit()

6. isalnum()
Devuelve True si la cadena es todo números o carácteres alfabéticos:
c = "ABC10034po"
c.isalnum()

7. isalpha()
Devuelve True si la cadena es todo carácteres alfabéticos:
c = "ABC10034po"
c.isalpha()

8. islower()
Devuelve True si la cadena es todo minúsculas:
"Hola mundo".islower()

9. isupper()
Devuelve True si la cadena es todo mayúsculas:
"Hola mundo".isupper()

10. istitle()
Devuelve True si la primera letra de cada palabra es mayúscula:
"Hola Mundo".istitle()

11. startswith()
Devuelve True si la cadena empieza con una subcadena:
"Hola mundo".startswith("Mola")

12. endswith()
Devuelve True si la cadena acaba con una subcadena:
"Hola mundo".endswith('mundo')

13. replace()
Reemplaza una subcadena de una cadena por otra y la devuelve:
"Hola mundo".replace('o','0')
'H0la mund0'
