# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 

# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, 
# valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".

# 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos



#Ejercicio 1)
# userEmail = input("Dame tu email\n")
# def validarEmail(email):
#     if "@" in userEmail:
#         return "El email introducido es correcto"
#     else:
#         return "Email introducido no válido, debe contener un @"

# print(validarEmail(userEmail))



#Ejercicio 2)
# dniUser = input("Dame tu dni\n")

# def validarDni(dni):
#     if dni.isdigit():
#         if len(dni) >= 7 and len(dni) <= 8:
#             return True
#         else:
#             return False
#     else:
#         return "El dni solo debe contener numeros"

# print(validarDni(dniUser))



#------------------------------
# Investigación ejercicios Java
#------------------------------

#Ejercicio 1)
# import java.util.Scanner;

# class Main {
#   public static void main(String[] args) {
#     Scanner sc = new Scanner(System.in);
#     System.out.print("Decime tu nombre: ");
#     String nombre = sc.nextLine();
#     saludos(nombre);
#   }

#   public static void saludos(String nombre) {
#     System.out.println("Hola " + nombre + " como estas?");
#   }
# }


#Ejercicio 2)
# class Main {
#   public static int suma(int a, int b) {
#     return a + b;
#   }

#   public static void main(String[] args) {
#     int resultado = suma(5, 5);
#     System.out.println(resultado);
#   }
# }
