# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 

# 1. Solicitar al usuario que ingrese su dirección email.
#  Imprimir un mensaje indicando si la dirección es válida o no,
#  valiéndose de una función para decidirlo. Una dirección se considerará 
# válida si contiene el símbolo "@".

# def Valido_email (*emails):
#  contador = 0
#  for elemento in emails:
#      for caracter in elemento:
#         if caracter == "@":
#             contador += 1
#  return len(emails) == contador  

# emailUsuario = input("Ingrese su e-mail")
# if Valido_email(emailUsuario):
#     print("Es valido")
# else: 
#     print("No es valido")
 

#En Java seria: 
# import java.util.Scanner; 
# public class Main {
#     static boolean validarEmail(String email) {
#             return email.contains("@");
#         }
#     public static void main(String[] args) {      
#         Scanner entrada = new Scanner(System.in);
#         System.out.println("Por favor ingrese su e-mail");
#         String emailUsuario = entrada.nextLine();
#         if (validarEmail(emailUsuario)) {
#          System.out.println("Es un e-mail valido");
#         } else {
#          System.out.println("Es un e-mail invalido");
#         }
#         }
# }     

# 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido 
# y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos

# def Valido_DNI (*dni):
#  contador = 0
#  for elemento in dni:
#      if (len(elemento) == 7) or (len(elemento) == 8):
#       contador += 1
#  return len(dni) == contador  

# DNI = input("Ingrese su dni")
# if Valido_DNI(DNI):
#     print("Es valido")
# else: 
#     print("No es valido")   


# En Java seria:

# import java.util.Scanner;
 
# public class Main {
    
#     public static int cuentaCifras(int num) {
#     int contador = 0;
#     if (num == 0) {
#         contador = 1;
#     } else {
#         for (int i = Math.abs(num); i > 0; i /= 10) {
#             contador++;
#         }
#     }
#     return contador;
#     }
#     public static void main(String[] args) {
#         Scanner entrada = new Scanner(System.in);
#         System.out.println("Introduce tu dni");
#         int dni = entrada.nextInt();
#         if ((cuentaCifras(dni) == 7) || (cuentaCifras(dni) == 8)){
#          System.out.println("Es un dni valido");
#         } else {
#          System.out.println("Es un dni invalido");
#      }

#     }
# }

