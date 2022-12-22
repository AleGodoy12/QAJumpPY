# 1. Escribir un programa que muestre por pantalla la cadena de texto.
a = 'Texto'
print(a)

# 2. Declare una variable que en su valor contenga un digito como cadena de texto
b = '1'

# 3.  Declare una variable con su nombre, otra con su apellido y concatenelas para mostrar por consola.
nombre = 'Gabriel'
apellido = 'Narvaez'
print(nombre, apellido)

# 4. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
#  muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombreUser = input('Ingrese su nombre\n')
print(f'¡Hola {nombreUser}!')


# 5. Declare una variable cuyo valor sea el numero 2, otra variable cuyo valor sea el numero 10 y realice las operaciones aritmeticas basicas 
# (suma, resta, multiplicacion y division), mostrando el resultado de cada una de ellas por pantalla. 
num1 = 2
num2 = 10
print(f'La suma de los números es: {num1+num2}\nLa resta de los números es: {num1-num2}\nLa multiplicación de los números es: {num1*num2}\nLa división de los números es: {num1/num2}')

#------------------------------
# Investigación ejercicios Java
#------------------------------

# 1)
# public class Main {
#   public static void main(String[] args) {
#     String a = "Texto";
#     System.out.println(a);
#   }
# }

# 2)
# String b = "1";

# 3)
# public class Main {
#   public static void main(String[] args) {
#     String nombre = "Gabriel";
#     String apellido = "Narvaez";
#     System.out.println(nombre + " " + apellido);
#   }
# }

#4)
# import java.util.Scanner;
# public class Main {
#   public static void main(String[] args) {
#     Scanner scanner = new Scanner(System.in);
#     System.out.print("Ingrese su nombre: ");
#     String nombreUser = scanner.nextLine();
#     System.out.println("¡Hola " + nombreUser + "!");
#   }
# }

#5)
# public class Main {
#   public static void main(String[] args) {
#     int num1 = 2;
#     int num2 = 10;
#     System.out.println("La suma de los números es: " + (num1 + num2));
#     System.out.println("La resta de los números es: " + (num1 - num2));
#     System.out.println("La multiplicación de los números es: " + (num1 * num2));
#     System.out.println("La división de los números es: " + (num1 / num2));
#   }
# }