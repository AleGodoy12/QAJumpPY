#En la carpeta con tu nombre, agregar un archivo .py con la resolucion de cada una de las consignas.
#Recorda investigar y comentar la resolucion en java

# 1. Escribir un programa que muestre por pantalla la cadena de texto.

# 2. Declare una variable que en su valor contenga un digito como cadena de texto

# 3. Declare una variable con su nombre, otra con su apellido y concatenelas para mostrar por consola.

# 4. Escribir un programa que pregunte el nombre del usuario en la consola 
#y después de que el usuario lo introduzca muestre por pantalla 
#la cadena ¡Hola !, donde es el nombre que el usuario haya introducido.

# 5. Declare una variable cuyo valor sea el numero 2, 
#otra variable cuyo valor sea el numero 10 y realice las operaciones aritmeticas basicas (suma, resta, multiplicacion y division)
#mostrando el resultado de cada una de ellas por pantalla.


# 1.
print("hola mundo")

# 2.
dni = "Lara44678987"
print(dni.isalpha())
print(dni.isalnum())

# 3.
Nombre = "Lara"
Apellido = "Ramirez"
print(Nombre + " " + Apellido)

# 4.
Nombre_usuario = input("Ingrese su nombre")
print("¡Hola" + " " + Nombre_usuario + "!")

# 5.

Num1 = 2
Num2 = 10
print (Num1 + Num2)
print (Num1 - Num2)
print (Num1 * Num2)
print (Num1 / Num2)