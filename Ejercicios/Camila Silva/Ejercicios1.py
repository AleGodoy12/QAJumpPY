#1. Escribir un programa que muestre
# por pantalla la cadena de texto.

Saludo = "Hola Mundo!"
print(Saludo)

# En Java seria:
# public class ImprimirCadena {
#     public static void main(String args[]) {

#       System.out.println("Hola Mundo!");
#     }
# }

#2. Declare una variable que en su valor contenga
# un digito como cadena de texto

omnibus_linea = "101"

# En Java seria:
# public class PrimeraVariable
# {
# public static void main ( String[] args ) { 
#    String mensaje = "101";
#  }
# }


#3. Declare una variable con su nombre, otra con su apellido y
# concatenelas para mostrar por consola.

Nombre = "Camila"
Apellido = "Silva"

print(Nombre + " " + Apellido)

# En Java seria:
# public class ConcatenacionDeTexto
# {
# public static void main ( String[] args ) { 
    # String nombre = "Camila";
     # String apellido = "Silva";
     # System.out.println(nombre + " " + apellido);
#  }
# }



#4.Escribir un programa que pregunte el nombre del usuario en la consola y 
# después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, 
# donde <nombre> es el nombre que el usuario haya introducido.

Nombres = input("Introduzca su nombre")
print("¡Hola " + Nombres+ "!")

# En Java seria:
# import java.util.Scanner;
# public class ConcatenacionDeTexto
# {
# public static void main ( String[] args ) { 
    # Scanner entrada = new Scanner(System.in)
    # System.out.println("Por favor ingrese su nombre");
    #String nombre = entrada.nextLine(); 
    #System.out.println("¡Hola " + nombre + "!");
#  }
# }


#5- Declare una variable cuyo valor sea el numero 2, otra variable cuyo valor sea el numero 10 y realice las operaciones aritmeticas basicas (suma, resta, multiplicacion y division), mostrando el resultado de cada una de ellas por pantalla. 
Numero = 2
Numero2 = 10
suma = Numero2+Numero
resta = Numero2-Numero
multiplicacion = Numero2*Numero
division = Numero2/Numero
print("La suma de los numeros " + str(Numero2) + " y " + str(Numero) + " es " + str(suma))
print("La resta de los numeros " + str(Numero2) + " y " + str(Numero) + " es " + str(resta))
print("La multiplicacion de los numeros " + str(Numero2) + " y " + str(Numero) + " es " + str(multiplicacion))
print("La division de los numeros " + str(Numero2) + " y " + str(Numero) + " es " + str(division))

# En Java seria:
#  public class OperacionesAritmeticas
#  {
#  public static void main ( String[] args ) { 
#       int numero = 2;
#       int numero2 = 10;
#       int suma = numero2 + numero;             
#       int resta = numero2 - numero;            
#       int multiplicacion = numero2 * numero;   
#       double division = numero2 / numero;  
#      System.out.println("La suma de los numeros " + numero2 + " y " + numero + " es " + suma);
#      System.out.println("La suma de los numeros " + numero2 + " y " + numero + " es " + resta);
#      System.out.println("La suma de los numeros " + numero2 + " y " + numero + " es " + multiplicacion);
#      System.out.println("La suma de los numeros " + numero2 + " y " + numero + " es " + division);
#  }
# }


