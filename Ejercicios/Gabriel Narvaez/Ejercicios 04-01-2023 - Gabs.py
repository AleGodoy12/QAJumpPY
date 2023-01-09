# # Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 
# # Agregar en JAVA los ejercicios hechos en clase.

# 1. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos 
# y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# 2. Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
# y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
# donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

# 3. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
# y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. 
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.



#Ejercicio 1)
# frutas = {"Manzana":10,"Pera":20,"Banana":30,"Naranja":40}
# userFruta = input("Que fruta querés?").title()

# if userFruta in frutas:
#     userFrutaKg = float(input("Cuantos kg?"))
#     print(f'El valor de {userFrutaKg} Kg de {userFruta} es {frutas[userFruta]*userFrutaKg}$, el precio por Kg es: {frutas[userFruta]}$')
# else:
#     print('No se encontró la fruta que buscabas')



#Ejercicio 2)
# asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
# creditosTotales = 0

# for i in asignaturas.keys():
#     creditosTotales+=asignaturas[i]
#     print(f'{i} tiene {asignaturas[i]} creditos')
# print(f'Los creditos totales son: {creditosTotales}')



#Ejercicio 3)
# palabraUser = input('Bienvenido al diccionario, ingrese su juego de palabras español:inglés\nPor ejemplo: "Pan:Bread"\nSi desea agregar mas palabras, puede hacerlo separandolas con una coma\nPor ejemplo: "Pan:Bread,Manzana:Apple"\n')
# listaUser = palabraUser.split(",")
# diccionarioUser = {}
# for i in listaUser:
#     listaUser = i.split(":")
#     diccionarioUser[listaUser[0].title()] = listaUser[1].title()
# palabraUser = input("Decime que palabra querés traducir de español a inglés:\n")
# if palabraUser.title() in diccionarioUser.keys():
#     print(f'La traducción de {palabraUser.title()} es {diccionarioUser[palabraUser.title()]}')
# else:
#     print("No tenemos esa palabra en el diccionario")



#------------------------------
# Investigación ejercicios Java
#------------------------------

#Ejercicio 1)

# import java.util.Scanner;
# import java.util.Map;
# import java.util.HashMap;

# class Main {
#     public static void main(String[] args) {
#     Map<String, String> moneda = new HashMap<String, String>();
#     moneda.put("Euro", "IconoDelEuro(?");
#     moneda.put("Dollar", "IconoDelDolar(?");
#     moneda.put("Yen", "IconoDelYen(?");

#     Scanner sc = new Scanner(System.in);
#     System.out.print("Decime la divisa: ");
#     String consulta = sc.nextLine();

#     if (moneda.containsKey(consulta)) {
#         System.out.println(moneda.get(consulta));
#     } else {
#         System.out.println("No lo encontro");
#     }

#     }
# }

#Ejercicio 2)

# import java.util.Scanner;
# import java.util.Map;
# import java.util.HashMap;

# class Main {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
#         System.out.print("Decime tu nombre: ");
#         String nombre = sc.nextLine();
#         System.out.print("Decime tu edad: ");
#         int edad = sc.nextInt();
#         sc.nextLine();  
#         System.out.print("Donde vivis? ");
#         String direccion = sc.nextLine();
#         System.out.print("Numero de telefono: ");
#         int telefono = sc.nextInt();

#         Map<String, Object> persona = new HashMap<String, Object>();
#         persona.put("nombre", nombre);
#         persona.put("edad", edad);
#         persona.put("direccion", direccion);
#         persona.put("telefono", telefono);
#         System.out.println(persona.get("nombre") + " tiene " + persona.get("edad") + " anios, vive en " + persona.get("direccion") + " y su numero de telefono es " + persona.get("telefono"));
#     }
# }