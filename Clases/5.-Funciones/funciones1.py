# def saludo (nombre):
#       saludando = print("Hola" + nombre + "Como estas?")
#       return saludando
# nombre = input("Ingrese nombre")
# saludo(nombre)


def saludos(nombre):
     #nombre = input("Ingrese su nombre")
     saludando = print("Hola" + nombre + " como estas?")
     return saludando
nombre = input("Ingrese su nombre")
print(saludos(nombre))
saludos(nombre)

#-------


def suma(a, b, c=0):
    return a+b+c
print(suma(5,5,3))