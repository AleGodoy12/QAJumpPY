# 1. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos 
# de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

preciosfrutas={"Banana":120,"Manzana":200,"Naranja":100,"Frutilla":120,"Kiwi":60,"Durazno":50,"Pera":80}
frutaUser=input("Ingrese la fruta que desea comprar:")
kilosUser=int(input("Ingrese el kg de fruta que desea comprar:"))
if frutaUser.title() in preciosfrutas:
     precio=(kilosUser*preciosfrutas[frutaUser.title()]);
     print('El precio es:',precio)
     print('para kilo ',kilosUser)
else:
    print("La fruta seleccionada no esta en la lista")

# 2. Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5}
#  y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> 
# créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos.
#  Al final debe mostrar también el número total de créditos del curso.

asignaturas_creditos={'Matemáticas': 6, 'Física': 4, 'Química': 5}
suma=sum(asignaturas_creditos.values()) 
for x,y in asignaturas_creditos.items():
    print('La asignatura',x, 'tiene',y,'creditos') 
    print('El total de los creditos del curso es:',suma)

# 3. Escribir un programa que cree un diccionario de traducción español-inglés.
#  El usuario introducirá las palabras en español e inglés separadas por dos puntos,
#  y cada par <palabra>:<traducción> separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. 
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.

diccionario={}
palabraUser=input("Ingrese una palabra en español y su traduccion en ingles con el formato <<palabra:traduccion>>")
for i in palabraUser.split(","):
    clave,valor= i.split(":")
    diccionario[clave]=valor
frase=input('Escribe la frase en español para traducirlo:')
for x in frase.split(" "):
    if x in diccionario:
        print(diccionario[x])
    else:
        print(x)
# moneda = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# consulta = input("Decime la divisa")
# if consulta.title() in moneda:
#    print(moneda[consulta.title()])
# else:
#     print("No lo encontro")
#JAVA
# package com.map;
# import java.util.Map;
# import java.util.HashMap;
# import java.util.Scanner;
# class divisas{
#     public static void main(String[] args) {
#   Map<Integer,String> monedas= new HashMap<>();
#   monedas.put('Euro','€');
#   monedas.put('Dollar','$');
#   monedas.put('Yen','¥');
#   Scanner divisa = new Scanner (System.in);
#   System.out.println("Ingrese una divisa: ");
#   String divisa = divisa.next();
#    if(divisa==monedas) {
#        System.out.println(monedas.getValue()); 
#     } else {
#       System.out.println("No existe la divisa"); 
#       }

#     }
# }

# nombre = input("Decime tu nombre")
# edad = int(input("Decime tu edad"))
# direccion = input("Donde vivis?")
# telefono = int(input("Numero de telefono"))
# Persona = {"nombre": nombre , "edad": edad, "direccion": direccion, "telefono": telefono}
# print(Persona['nombre'], 'tiene', Persona['edad'], 
# 'años, vive en', Persona['direccion'], 
# 'y su número de teléfono es', Persona['telefono'])
#JAVA
# package com.map;
# import java.util.Map;
# import java.util.HashMap;
# import java.util.Scanner;
# class Persona{
#     public static void main(String[] args) {
#         Scanner entrada= new Scanner(System.in)
#         String nombre;
#         System.out.print("Ingrese su nombre:");
#         nombre=entrada.next();
        
#         Scanner entrada= new Scanner(System.in)
#         String direccion;
#         System.out.print("Ingrese su direccion:");
#         direccion=entrada.next();
        
#         Scanner entrada= new Scanner(System.in)
#         int edad;
#         System.out.print("Ingrese su edad:");
#         edad=entrada.nextInt(); 
        
#         Scanner entrada= new Scanner(System.in)
#         int telefono;
#         System.out.print("Ingrese su telefono:");
#         telefono=entrada.nextInt();
        
#         HashMap<String,Integer> Persona = new HashMap ();
#         persona.put("Nombre",nombre);
#         persona.put("Direccion",direccion);
#         persona.put("Edad",edad);
#         persona.put("telefono",telefono);
        
#         System.out.println(persona.get("Nombre") + 'tiene' + persona.get("Edad") + 'años,vive en' + persona.get("Direccion") + 'y su numero de telefono es' + persona.get("telefono"));
#     }
# }
