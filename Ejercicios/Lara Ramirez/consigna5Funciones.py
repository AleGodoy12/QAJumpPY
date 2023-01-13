# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 

# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, 
# valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".

# 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos


# EJERCICIO 1

#def valido (email):
#    if email.count ("@gmail.com"):
#        si = print ("El mail fue validado con éxito")
#    else:
#        no = print ("El mail ingresado no es válido")
#    return valido
#email = input ("Ingrese su Email  ")
#print (valido(email))

# EJERCICIO 2

def contar(dni):
    if len(dni.strip()) >= 7 and len(dni.strip()) <= 8:
        print ("Válido")
    else:
        print ("No válido")
    return len(dni.strip())


dni = input ("Ingrese su dni sin puntos ni espacios   ")
contar(dni)

