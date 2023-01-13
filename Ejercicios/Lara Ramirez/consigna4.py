# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 
# Agregar en JAVA los ejercicios hechos en clase.

#1. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#2. Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla 
# los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> 
# es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
# Al final debe mostrar también el número total de créditos del curso.

#3. Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> 
# separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. 
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.

## EJERCICIO 1

#frutas = {'Manzana': 100, 'Banana':150, 'Durazno':200, 'Naranja':70}
# consulta = input ("Ingrese una fruta  ")
#kilos = int (input ("Ingrese una cantidad de kilos  "))
#if consulta.title() in frutas:
#    print ("El valor de su compra es $", (frutas[consulta.title()])*kilos,)
#else:
#    print ("La fruta ingresada no fue encontrada")

## EJERCICIO 2

#materias = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
#consulta = input ("Ingrese una asignatura  ")
#if consulta.title() in materias:
#    print (consulta.title(), "tiene ", (materias[consulta.title()]), "créditos")
#    print ("El curso total tiene ", (6+4+5), "créditos")
#else:
#    print ("No se encontró la asignatura")

## EJERCICIO 3

diccionario = {}
palabras = input ("Ingrese las palabras en español y su traducción al inglés, para separar palabras use ':' y para separar pares ','-> ")
for i in palabras.split (','):
    clave, valor = i.split (':')
    diccionario [clave] = valor
frase = input ("Introduce una frase en español: ")
for i in frase.split():
    if i in diccionario:
        print (diccionario[i], end = " ")
    else:
        print (i, end= " ")

# En este último ejercicio no pude resolver porqué el programa me toma solo una palabra