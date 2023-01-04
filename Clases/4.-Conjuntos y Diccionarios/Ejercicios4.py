#Escribir un programa que guarde en una variable
#  el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o 
# un mensaje de aviso 
# si la divisa no está en el diccionario.

#Declaro una lista de monedas que contenta este dict 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

# moneda = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# consulta = input("Decime la divisa")
# if consulta.title() in moneda:
#      print(moneda[consulta.title()])
# else:
#      print("No lo encontro")

# monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# moneda = input("Introduce una divisa: ")
# print(monedas.get(moneda.title(), "La divisa no está."))

# Escribir un programa que pregunte al usuario su nombre, 
# edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> 
# tiene <edad> años, vive en <dirección> y 
# su número de teléfono es <teléfono>.

nombre = input("Decime tu nombre")
edad = int(input("Decime tu edad"))
direccion = input("Donde vivis?")
telefono = int(input("Numero de telefono"))

Persona = {"nombre": nombre , "edad": edad, "direccion": direccion, "telefono": telefono}
# print(nombre, "tiene ", edad, "años, vive en" ,direccion ,
#       "y su numero de telefono es:", telefono)
# print(Persona.get(nombre))
print(Persona['nombre'], 'tiene', Persona['edad'], 
'años, vive en', Persona['direccion'], 
'y su número de teléfono es', Persona['telefono'])