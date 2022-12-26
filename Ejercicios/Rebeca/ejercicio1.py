#1) Escribir un programa que muestre por pantalla la cadena de texto.
#saludo="hola Rebe"
#print(saludo)

"""
equivalente en Java
public class saludo {
    public static void main(String[] args) {
      String hola="hola Rebe";
      System.out.print(hola);
      }
}

"""
#2) Declare una variable que en su valor contenga un digito como cadena de texto
nombre = "Pedro"
edad = 12
#print("Me llamo", nombre, "y este mes cumplo", edad, "años.")



"""
public class saludo {
    public static void main(String[] args) {
         //System.out.println("Sum of x+y = " + z);
      String saludo="hola Rebe";
      System.out.print(saludo+ " ¿cómo estás?");
      }
}
"""

#3) Declare una variable con su nombre, otra con su apellido y concatenelas para mostrar por consola.
a = "Rebeca"
b = "Barrios"
#print("Buen día. Me llamo", a, "y mi apellido es",b, ".")

#equivalente en Java
"""
public class Main {
    public static void main(String[] args) {
    String a="Rebe";
    String b="Barrios";
      System.out.print("Hola, mi nombre completo es: "+ a+","+b);
      
  }
}

"""




#4) Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
#nombre=input("Por favor, ingrese su nombre:")
#print ("Hola,",nombre)

#equivalente en Java
"""
import java.util.Scanner;
public class Main
{
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
    String nombre="";
      System.out.println("Por favor, ingrese su nombre:");
      nombre = entrada.nextLine();
      System.out.print("Hola,"+nombre);
    
         
    }
}

"""



#5)  Declare una variable cuyo valor sea el numero 2, otra variable cuyo valor sea el numero 10 y realice las operaciones aritmeticas basicas (suma, resta, multiplicacion y division), mostrando el resultado de cada una de ellas por pantalla. 
num1=2
num2=10
suma=num1+num2
resta=num1-num2
mult=num1*num2
div=num2/num1
print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicación es: ",mult)
print("La división es: ",div)

#equivalente en Java

"""
public class Main
{
    public static void main(String[] args) {
        int suma, resta, mult,div;
       
        int num1 = 2;
        int num2 = 10;
        suma = num1+num2;
        resta = num1-num2;
        mult = num1*num2;
        div = num2/num1;
        
        System.out.println("La suma es:"+ suma+" y la resta es:"+ resta);
        System.out.println("La multiplicaión es:"+ mult+". Y la división es:"+div);
        
    }
}

"""