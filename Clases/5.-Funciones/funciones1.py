# def saludo (nombre):
#       saludando = print("Hola" + nombre + "Como estas?")
#       return saludando
# nombre = input("Ingrese nombre")
# saludo(nombre)


# def saludos(nombre):
#      #nombre = input("Ingrese su nombre")
#      saludando = print("Hola" + nombre + " como estas?")
#      return saludando
# nombre = input("Ingrese su nombre")
# print(saludos(nombre))
# saludos(nombre)

# #-------


# def suma(a, b, c=0):
#     return a+b+c
# print(suma(5,5,3))

# *args

# def funcion(arg1, arg2, arg3, arg4):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#     print(arg4)
# funcion(1,2,"hola",4)

# def funcion1(*args):
#      print(args)
# funcion1("hola", 1.2, 4, "chao", 2, "hola1")

# def funcion1(*args):
#      for i in args:
#       print(i)
# funcion1("hola", 1.2, 4, "chao")

# def total(*args):
#     total = sum(args)
#     print(total)
# total(200,300,100,700,12,40)


#**kwargs

# def empleado(nombre, puesto, lenguaje):
#      print(nombre)
#      print(puesto)
#      print(lenguaje)
# empleado("Ana", "QA Automation", "Java")
# #Keyword arguments
# def empleado(nombre, puesto, lenguaje):
#      print(nombre)
#      print(puesto)
#      print(lenguaje)
# empleado(nombre= "Ana", puesto= "QA Automation", lenguaje="Java")

# def empleado(b, *args, **kwargs):
#      for key, value in kwargs.items():
#          print(f"{key} : {value}")
# empleado(nombre= "Ana", puesto= "QA Automation", lenguaje="Java")

# #recursividad

def cuenta_Regresiva(numeros):
     numeros -= 1
     if numeros > 0:
         print(numeros)
         cuenta_Regresiva(numeros)
     else:
        print("Salimos")
    
cuenta_Regresiva(20)
