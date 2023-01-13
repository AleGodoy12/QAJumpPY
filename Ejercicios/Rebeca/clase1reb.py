#______________________________________ CLASE 6_____________________________
# FUNCIONES 2 
'''
def resta(a, b):
    return a-b
result=resta(b=15,a=12)
result;


def resta(a=10, b=5):
    return a-b
result=resta()
print result;

'''
#paso or valor, se crea una copia local de la variable de l funcion
#uso de Args
'''
def suma(*args):
    s=0
    for arg in args:
        s+=arg
    return s

suma(1,3)
#salida 10

#suma(1,1)
#salida 2
'''
'''
def suma(*args):
    return sum(args)

suma(15,5)

#por ref: 

'''
'''
def funcion(arg1, arg2,arg3,arg4 ):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)
funcion(1,2,"hola", 4)


'''
















#______________________________________ CLASE5_____________________________
# FUNCIONES, VALORES, RETORNO
#agrupaciones de código. Todo lo que tenemos como repsuesta de ejecución se llama RETORNO.
#DEF palabra reservada
#DEF NOMBRE(parám): 
#   sentencias  : bloque de pantalla
#   RETORN: indica que devolver cuando llamamos la función. Con esto finalizo el bloque de código 

def saludar():
    print('estoy saludando desde la función')

#la llamo
#saludar()

'''
def saludar_nombre(nombre):
    saludando=print("Hola {}! como estás?".format(nombre))
    return saludando

saludar_nombre("Juan")
'''
'''
def lista():
    return[1,2,3,4,5]
    print(lista)[1:3]
'''
'''
def suma(num1, num2):
    return num1+num2
#r=suma(7,5)

#print(suma(2,3))
print(input("ingrese dos numeros"))

'''
'''
def saludo(nombre):
    print("Hola", nombre)
    return None
    
nombre_usuario=input("Introduzca su nombre:")
  
saludo()

'''

'''
def saludos(nombre):
    #nombre=input("Ingrse nomnbre")
    saludando=print("Hola"+nombre)
    return saludando

nombre=input("Ingrese nombre")
saludos(nombre)

'''













#______________________________________ CLASE4_____________________________
# CONJUNTOS Y DICCIONARIOS
# conjunto o SET no ordenada de objetos UNICOS, no tiene elementos duplicados
#heterogéneas. No puede contener objetos mutables, podemos incluirlos pero ya no la podré modificarla, tendría que sacarla moficicarle y volverla a incluir.
#SET: se puede convertir de SET a LISTA y viceversa
conjunto={1,2,3,4,"hola"}

conj=list({1,2})
#print(conj)

#Set vs Lista


#Funcionaes integradas
#1 ADD

num={1,2,3,4}
#num.add(5)
#print(num)

#2 UPDATE: agtega multiples aelementos
#num.update([5,6])
#num.update(range(9,12))
#print(num)

#3 LONGITUD DEL SET

#4 DISCARD(): elimina el item del set. IMPORTANTE
#num.discard(2)
#print(num)

#5 REMOVE: si el item a remover no existe simplemente se ignora. Nos indicará un ERROR
#num.remove(4)
#print(num)   

#IN: para determinar si un elemento pertenece al set. TRU o False
#2 in num       verrrr

#7 CLEAR: elemina el contenido pero no la estructura
#num.clar

#8 POP: retorna un elemnto en forma aleatoria, ya que los elem. no están ordenados.
#while num:
#    print("se esta borrando:", num.pop())
#print(num)     #consultar....

#Diccionarios: coleccion NO ORDENADAS de objetos. Para identificarlo especif una clave, no por su posicion
#las claves suelen ser INT o STRING
#trabajamos sobre la clave o sobbre el valor??????. Usualmente cambiamos el nombre de la clave, no del valor.

colores={"amarillo":"yellow", "azul":"blue"}
#print(colores["amarillo"])  #me imprime "yellow"

#Indice: comienza en CERO. Posicion: inicia en 1 OJO

#MUTABILiDAD

#ASIGNACION
edades={"Juan":26,"Esteban":35}
#edades["Juan"]+=5
#print(edades["Juan"])

#FUNCIONES
#ADD 
#UPDATE
#colores.update({"cinco":5})
#print(colores)

#LEN: longitud                              
#print(len(colores))

#DEL: elimina el item del dict, sin modificar el resto de dict. Si no está, se ignora
#del edades["Esteban"]
#print(edades)

#IN: el valor es mutable, entonces siempre validades por CLAVE no por valor

#CLEAR: BOrra TODOS los valores de uin dict. Elimina el valor NO LA ETIQUETA, es decir seguiré teniendo la variable.
numeros={"uno":1,"dos":2,"tres":3}
#numeros.clear()
#numeros={}    #es otra manera de hacerlo
#print(numeros)


#Ejercicios:
monedas={"Euro":'#',"Dollar":'$',"Yen":'%'}
#user=input("decime la divisa")
'''
#una forma
if user.title() in monedas:
    print("encontrado")
else:
    print("no lo encontro")

'''
#otra forma, usando .GET, para que me devuelva su valor
#print(monedas.get(user.title(), "La divisa no está"))  #busca por asociacion de CLAVE y me devuelve su VALOR

#otra forma
#if user.title() in monedas:
#    #print("encontrado")
#    #print(monedas.get(user.title(), "La divisa no está"))
#    print(monedas[user.title()])
#else:
#    print("no lo encontro")

#Ejercicios
'''
nombre=input("ingrese nombre")
edad=int(input("ingrese edad"))
#dir=input("Ingrese dirección")
#tel=int(input("Ingrese telefono"))

datos={"nombre": nombre,"edad": edad}
#print(nombre, "tiene", edad, "años")
print(datos['nombre'], "tiene", datos['edad'])  #MEJOR UTILIDAD, codigo reutilizable

#pasar estos dos ejercicios a JAVA y subir a la carpeta


'''

















#______________________________________ CLASE4_____________________________
# CONTROLADORES 2: While

#While-Else
#1 break: el programa cierra el bucle por completo
#2 continue: el prog omite parte del bucle antes de continuar
#3 pass: ignore ese factor externo
'''
chance=1
while chance<=3:
    txt =input('Escribe SI:')
    if txt=='SI':
        print('Ok, lo conseguiste en el intento',chance)
        break
    chance +=1
else:
    print('Has agotado tus tres intentos')
'''


#Ejemplo 1 con break
'''
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
'''
#Ejemplo 2 con continue
'''
#                               consultar como funciona esto...
i=1
while i<6:
    print(i)
    if i==3:
        continue
    i+=1
'''

#Sentencia FOR. Diremos "for valor in lista_de_valores"
lista=[1,2,3,4,5]
#ejmplo1
#for valor in lista:
#    print('Soy un item de la lista y valgo',valor)

#for num in lista:
#    print('Soy un valor de la lista y valgo', num)
#    num *=5
#    print('Soy un valor de la lista y ahora valgo', num)

#ejmplo2
indice=0
numbers=[0,1,2,3,4,5,6,7,8,9,10]
#for num in numbers:
#    numbers[indice]*=5
#    indice +=1
#    print(numbers)   #no entendí como funciona (?)

#DICCIONARIOS: 







#______________________________________ CLASE3_____________________________
# CONTROLADORES 1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no. 
'''
edad=int(input("Ingrese su edad"))
if edad <18:
   print("Eres menor de edad")
else: 
    print("Eres mayor de edad")

'''

#Escribir un programa que almacene la constraseña de caracteres contraseña 
#en una variable, pregunte al usuario por la contraseña e imprima por pantalla
# si la constrseña introducida por el usuario coincide con la guardada en la 
#variable sin tener en cuenta mayúsculas ni minúsculas


var='contraseña'
contraseña=input('Ingrse la contraseña')
if contraseña.lower()==var:
    print("La contraseña es igual")
else:
    print("La contraseña no coincide")





#______________________________________ CLASE2_____________________________
#LISTAS: esttrutura de datos que agrupa distintos elementos de una forma ordenada.
#heterogénea. Comienza con índice 0.

datos=[1,-5,123,34,'Una cadena','Otra cedena','Pepito']
#print (datos[0])
#print (datos[-3:])     #esto es Slicing

num=datos+[1,2]          #así concateno
#print (num)   

# Asignación por Slicing: ya que las listas son mutables
letras=['a','b','c','d','e','f']   
letras[:3]=['A','B','C']    
#print(letras)

#Borrar valores por slicing
letras=[]
#print(letras)

#FUNCIONES 
#1Append: agrega item al final de la lista
datos.append(2)
#print(datos)

#2 Len: longitud
num=[1,2,3,4]
#print(len(num))

#3 Pop: elimina el último item de la lista. Funciona con índices
#num.pop()
num.pop(0)
#print(num)


#4 Count
nume=[1,2,3,1,4,1,5]
#print(nume.count(1)) 

#5 Index: nos dice en qué indice se encuentra
#print(nume.index(3)) 

#TUPLAS: heterogéneas, inmutables. No funciona Append, Pop. 
#funciona usar: LEN, Count, Index
nume=(1,2,3,1,4,1,5)
#print(nume)

#Borrar Valores
#nume=()
#print(nume)


#----------------- espacio para la tarea CLASE 2--------------------------
#1) 
Materias=['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
#print(Materias)

#2)
#Materias.append(2)
#print(Materias)

#print(len(Materias))

#Materias.pop(2)
#Materias.pop()
#print(Materias)

#Materias.append('Historia')
#print(Materias)
#print(Materias.count('Historia')) 

#print(Materias.index("Lengua"))


#3)
Receta=['harina','azúcar','banana','leche']
#print(Receta)
Receta2=tuple(Receta)
#print(Receta2)





#______________________________________ CLASE1_____________________________
#print("hola Mundo")

#saludo="hola mundo"
#print(saludo)

#nombre=input("ingrese su nombre")
#print("hola "+ nombre)



      
    
