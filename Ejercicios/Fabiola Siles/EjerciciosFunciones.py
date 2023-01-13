# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 

#1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".
def emailValido(correo):
     if '@' in correo:
         print("El correo es valido")
     else:
         print("El correo es invalido")

correo= input("por favor ingrese su correo electronico: ")
emailValido(correo)
#2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos
def esDNIvalido(dni):
    if (len(dni)==7 or len(dni)==8):
        return True
    else:
        return False

dni=(input("Por favor ingrese su dni:"))
print(esDNIvalido(dni))
