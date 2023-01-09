#1.Declare una variable con su nombre, otra con su apellido y concaténelas para mostrar por consola.
nombre="Natalia"
apellido="Sanabria"
print("Hola soy",nombre , apellido)

# 2.Declare una variable cuyo valor sea el numero 2, otra variable cuyo valor sea el numero 10 
# y realice las operaciones aritmeticas basicas (suma, resta, multiplicacion y division)
#  mostrando el resultado de cada una de ellas por pantalla. 
nro1=10
nro2=2
print("Suma:")
print(int(nro1+nro2))
print("Resta:")
print(int(nro1-nro2))
print("Multiplicación:")
print(int(nro1*nro2))
print("División:")
print(int(nro1/nro2))

# 3.Escribir un programa que almacene una lista de ingredientes para hacer galletas y convierta dicha lista en una tupla.
lista_galletas= ["Harina","Mantequilla","Azucar","Bicarbonato","Esencia de vainilla"]
print("lista:", lista_galletas)
tuple(lista_galletas)
print("Tupla:")
print(tuple(lista_galletas))

# 4.Escribir un programa que muestre por pantalla la cadena de texto
texto="Hola, ¿como estas?"
print(texto)

# 5.Escribe un programa que sume dos variables y multiplique una tercera
nro1=20
nro2=30
nro3=10
suma= nro1+nro2
multi=suma*nro3
print("Suma:")
print(int(suma))
print("Multiplicación:")
print(int(multi))

# 6.Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla
asignaturas_lista=["Matemáticas", "Física", "Química", "Historia","Lengua"]
print(asignaturas_lista)

#7.Escriba un programa que almacene su nombre y apellido y muestre por pantalla el mensaje "Hola, *Nombre y apellido* Bienvenido"
nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
print("Hola " + nombre + " "+ apellido + " "+ "¡Bienvenido!")
#8.Declare una etiqueta que almacene un tipo de dato float
nrof= float(input(("Ingrese un decimal:")))
print(nrof)
#9.Declare una etiqueta que contenga una tupla con items que representen los 3 tipos de datos principales
tupla_lista=(100,"Hola soy un texto",10.3)
print(tupla_lista)
#10.Genere un programa que almacene una lista realice las siguiente operaciones:
# - Elimine el ultimo item.
# - Elimine el 2do item de derecha a izquierda.
lista=[1,2,3,4,5]
print(lista)
lista.pop()
print(lista)
lista.pop(-2)
print(lista)