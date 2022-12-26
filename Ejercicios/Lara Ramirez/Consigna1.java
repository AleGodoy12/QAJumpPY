//En la carpeta con tu nombre, agregar un archivo .py con la resolucion de cada una de las consignas.
//Recorda investigar y comentar la resolucion en java

// 1. Escribir un programa que muestre por pantalla la cadena de texto.

// 2. Declare una variable que en su valor contenga un digito como cadena de texto

// 3. Declare una variable con su nombre, otra con su apellido y concatenelas para mostrar por consola.

// 4. Escribir un programa que pregunte el nombre del usuario en la consola 
//y después de que el usuario lo introduzca muestre por pantalla 
//la cadena ¡Hola !, donde es el nombre que el usuario haya introducido.

// 5. Declare una variable cuyo valor sea el numero 2, 
//otra variable cuyo valor sea el numero 10 y realice las operaciones aritmeticas basicas (suma, resta, multiplicacion y division)
//mostrando el resultado de cada una de ellas por pantalla.


// 1.
public class HolaMundo
{
    public static void main(String[] args)
    {
        System.out.println("¡Hola mundo!");
    }
}

// 2.
public class Saludo
{
    public static void main(String[] args)
    {
        int saludo = "¡Hola mund0!"
        System.out.println(saludo);
    }
}

// 3.
public class Cuentas {
  public static void main (String args []) {
    int nombre = "Lara";
    int apellido = "Ramirez";

    System.out.println (nombre + apellido);
 }
}

// 4.
import java.util.Scanner;

public class Nombre {
  public static void main (String args []) {
    
    Scanner nombre = new Scanner (System.in);
    String nombre = Scanner.next ();

    System.out.println ("Ingrese su nombre");
    nombre = in.nextLine ();
    System.out.println ("¡Hola " + nombre + "!" );
 }
}

// 5.
public class Cuentas {
  public static void main (String args []) {
    int num1 = 2;
    int num2 = 10;
    int resultado = 0;

    resultado = num1 + num2;
    resultado = num1 - num2;
    resultado = num1 * num2;
    resultado = num1 / num2;
    System.out.println (resultado);
 }
}
