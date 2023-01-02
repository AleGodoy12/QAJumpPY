# En la carpeta con tu nombre, agregar un archivo .py con la resolucion de cada una de las consignas. 
# Recorda investigar y comentar la resolucion en java


# 1. Escribir un programa que muestre por pantalla la cadena de texto.
print("Bienvenid@, ¿Cómo estás?")

"""
Solución Java:

public class Ejercicio1 {
	public static void main(String[] arg) {
		System.out.print("Bienvenid@, ¿Cómo estás?");
	}
}

"""

#2. Declare una variable que en su valor contenga un digito como cadena de texto
nombre = "Bruno"
print("Mi nombre es:", nombre)

"""
Solución Java:

public class Ejercicio1 {
	public static void main(String[] arg) {
        String nombre = "Bruno";
		System.out.print("Mi nombre es: " + nombre);
	}
}
"""

#3.  Declare una variable con su nombre, otra con su apellido y concatenelas para mostrar por consola.
nombre_primero = "Bruno"
apellido = "Sena"
print("Hola soy:", nombre_primero, apellido)

"""
Solución Java:

public class Ejercicio1 {
	public static void main(String[] arg) {

        String nombre_primero = "Bruno";
        String apellido = "Sena";

        System.out.printf("¡Hola soy: %s %s!", nombre_primero, apellido);
	}
}
"""

#4. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
#muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombre_usuario = input("Bienvenido, ¿cómo te llamas?: ")
print(f"¡Hola {nombre_usuario}!")

"""
Solución Java:

import java.util.Scanner;

public class Ejercicio1 {
	public static void main(String[] arg) {

        Scanner teclado=new Scanner(System.in);

        String nombre;

		System.out.print("Bienvenido, ¿cómo te llamas?: ");
        nombre=teclado.next();

        System.out.printf("¡Hola %s!", nombre);
	}
}
"""

#5. Declare una variable cuyo valor sea el numero 2, otra variable cuyo valor sea el numero 10 y realice las operaciones aritmeticas basicas (suma, resta, multiplicacion y division), mostrando el resultado de cada una de ellas por pantalla.
num1 = 2
num2 = 10
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"Los resultados son: suma = {suma}, resta = {resta}, multiplicacion = {multiplicacion}, division = {division}")

"""
Solución Java:

public class Ejercicio1 {
    public static void main(String[] arg) {

        int suma, resta, multiplicacion;
        float division;
        int num1 = 2;
        int num2 = 10;
        suma = num1 + num2;
        resta = num1 - num2;
        multiplicacion = num1 * num2;
        division = num1 / num2;
        
        System.out.printf("Los resultados son: suma = %d, resta = %d, multiplicacion = %d, division = %f", suma, resta, multiplicacion, division);
        
    }
}
"""
