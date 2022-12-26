# En la carpeta con tu nombre, agregar un archivo .py con la resolucion de cada una de las consignas. 
# Recorda investigar y comentar la resolucion en java

#1. Escribir un programa que muestre por pantalla la cadena de texto.
texto='buen dia =)'
print(texto)

        #equivalente en java

# public class Main {
#   public static void main(String[] args) {
#     String texto = "buen dia =)";
#     System.out.println(texto);
#   }
# }


#2. Declare una variable que en su valor contenga un digito como cadena de texto
textoDigito= '10'

        #equivalente en java

# String textoDigito = "10";

#3.  Declare una variable con su nombre, otra con su apellido y concatenelas para mostrar por consola.
nombre= 'Fabiola'
apellido= 'Siles Valeriano'
print(nombre, apellido)

        #equivalente en java

# public class Main {
#   public static void main(String[] args) {
#     String nombre = "Fabiola";
#     String apellido = "Siles Valeriano;
#     System.out.println(nombre + " " + apellido);
#   }
# }

#4. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombre= input('Ingrese su nombre por favor\n')
print(f'¡Hola {nombre}!')

        #equivalente en java

# import java.util.Scanner;
# public class Main {
#   public static void main(String[] args) {
#     Scanner scanner = new Scanner(System.in);
#     System.out.print("Ingrese su nombre por favor: ");
#     String nombre = scanner.nextLine();
#     System.out.println("¡Hola " + nombre + "!");
#   }
# }


#5. Declare una variable cuyo valor sea el numero 2, otra variable cuyo valor sea el numero 10 y realice las operaciones aritmeticas basicas (suma, resta, multiplicacion y division), mostrando el resultado de cada una de ellas por pantalla. 
numUno= 2
numDos = 10
print(f'La suma es: {numUno+numDos}')
print(f'La resta  es: {numUno-numDos}')
print(f'La multiplicacion  es:{numUno*numDos}')
print(f'La division es:{numUno/numDos}')

        #equivalente en java

# public class Main {
#   public static void main(String[] args) {
#     int numUno = 2;
#     int numDos = 10;
#     System.out.println("La suma  es: " + (numUno+numDos));
#     System.out.println("La resta  es: " + (numUno-numDos));
#     System.out.println("La multiplicacion  es: " + (numUno*numDos));
#     System.out.println("La division  es: " + (numUno/numDos));
#   }
# }
