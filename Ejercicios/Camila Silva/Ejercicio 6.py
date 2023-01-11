# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 
# Agregar en JAVA los ejercicios hechos en clase.

# 1. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos
#  de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# PuestoFrutas = {'Manzana': 200, 'Frutilla':300, 'Banana':400}
# Fruta = input("Escribe la fruta que deseas")
# Kilos = int(input("Decime el kilo que deseas"))
# if (Fruta.capitalize() in PuestoFrutas) and (Kilos > 0):
#     print("El precio es ", PuestoFrutas[Fruta.capitalize()]*Kilos)
# elif (Fruta.capitalize() in PuestoFrutas) and (Kilos <= 0): 
#     print("La cantidad de kilos debe ser mayor a 0")
# else:
#     print("No encontramos la fruta que deseas")

# 2. Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
#  {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
#  asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las 
#  asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de
#   créditos del curso.

# Asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5} 

# sumacreditos = 0 
# for clave, valor in Asignaturas.items():
#     print(clave, "tiene", valor, "creditos")
# sumacreditos = sum(Asignaturas.values())    
# print("El total de creditos es", sumacreditos)


# 3. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras
#  en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa 
#  debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará
#   el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin 
# traducir.


# Traducciones = input("Debe introducir las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas.").split(",")
# DTraducciones = {}
# Error = ""
# for palabra in Traducciones: #Recorremos las palabras de la lista
#     if palabra.count(":") == 1: 
#         for indice in range(len(palabra)): #Recorremos con el indice los caracteres de la palabra
#             caracter = palabra[indice]
#             if caracter == ":":
#                 if(indice <len(palabra)-1) and (indice != 0):  #Si se completo todo
#                     Clave = palabra[:indice]
#                     Valor = palabra[indice+1:len(palabra)]

#                 elif(indice <len(palabra)-1) and (indice == 0):  #Si el ":" es el primer elemento. Ejemplo ":Hello"
#                     Valor = palabra[indice+1:len(palabra)]
#                     print(f"Te pedimos que nos ingreses la palabra en español de {Valor}")
#                     Clave = input()

#                 else: #El caso de ":" es el ultimo elemento.  Ejemplo "Hola:"
#                     Clave = palabra[:indice]
#                     print(f"Te pedimos que nos ingreses la palabra en ingles de {Clave}")
#                     Valor = input()
#                 DTraducciones[Clave.capitalize().strip()] = Valor.capitalize().strip()
#     else:  
#         Error += palabra + " "
# if len(Error)!= 0:
#  print("No pudimos ingresar las palabras", Error)
#  Error = " "       
# #Finalización de carga de datos al diccionario - Se continua solicitando al usuario una frase para traducir 
# Frase = input("Te pedimos que ingreses una frase para traducirla").strip().split()
# FraseTraducida = ""
# for elemento in Frase:
#     FraseTraducida += DTraducciones.get(elemento.capitalize(), elemento) + " "
# if len(FraseTraducida)!= 0:
#      print("La traduccion es", FraseTraducida.lower())
# else: 
#     print("No se ingreso ninguna frase")   



#Ejercicios de JAVA hechos en clase.

# import java.util.Hashtable;
# import java.util.Scanner;
 
# public class Main {
 
#     public static void main(String[] args) {
#         // De esta forma creo mi diccionario en java
#         Hashtable<String, String> monedas = new Hashtable<String, String>();
#         monedas.put("Euro", "Signo Euro");
#         monedas.put("Dollar", "Signo Dollar");
#         monedas.put("Yen", "Signo Yen");
#         Scanner entrada = new Scanner(System.in);
#         System.out.println("Por favor ingrese una moneda");
#         String moneda = entrada.nextLine();
#        if ( monedas.get(moneda) == null){
#         System.out.println("No se encuentra la moneda que busca");
#        }else {
#        System.out.println(monedas.get(moneda));
# }

 
#     }
# }


# import java.util.Hashtable;
# import java.util.Scanner;
 
# public class Main {
 
#     public static void main(String[] args) {
    
        
#         Scanner entrada = new Scanner(System.in);
#         System.out.println("Por favor ingrese su nombre");
#         String nombre = entrada.nextLine();
        
#         System.out.println("Por favor ingrese su direccion");
#         String direccion = entrada.nextLine();
        
#         System.out.println("Por favor ingrese su edad");
#             int  edad = entrada.nextInt();
        
#         System.out.println("Por favor ingrese su telefono");
#             int  telefono = entrada.nextInt();
            
       
#         Hashtable<String, Object> Persona = new Hashtable<String, Object>();
#         Persona.put("nombre", nombre);
#         Persona.put("edad", edad);
#         Persona.put("direccion", direccion);
#         Persona.put("telefono", telefono);
#         System.out.println(Persona.get("nombre") + " tiene " + Persona.get("edad") + " de edad, vive en " + Persona.get("direccion") + " y su numero de telefono es " +Persona.get("telefono") );
 

#     }
# }
