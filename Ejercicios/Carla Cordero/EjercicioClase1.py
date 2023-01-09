# En la carpeta con tu nombre, agregar un archivo .py con la resolucion de cada una de las consignas. 
# Recorda investigar y comentar la resolucion en java

# 1. 
print ("Hola, soy una cadena de texto!")

#En Java
#public class EjercicioClase1 {
#	public static void main(String[] arg) {
#		System.out.print("Hola, soy una cadena de texto!");
#	}
#}


#2. 
numero = "1"
print (numero)

# En Java
# public class EjercicioClase1 {
#   public static void main ( String[] args ) { 
#       String numero = "1";
#            System.out.print("El numero es: " + numero);
#   }
# }

#3.
nombre = "Carla"
apellido = "Cordero"
print ("Hola, mi nombre es:", nombre, apellido)

#En Java
# public class EjercicioClase1 {
#   public static void main ( String[] args ) { 
#       String nombre = "Carla";
#       String apellido = "Cordero";
#        System.out.print("Mi nombre es: " + nombre + " " + apellido);
#   }
#}

#4. 
nombreUsuario = input ("Ingrese su nombre : ")
print("¡Hola ", nombreUsuario, "!")

#En Java
# import java.util.Scanner;
# public class EjercicioClase1
# {
# public static void main ( String[] args ) { 
#     Scanner entrada = new Scanner(System.in);
#     System.out.println("Ingrese su nombre : ");
#     String nombre = entrada.nextLine(); 
#     System.out.println("¡Hola " + nombre + "!");
#  }
# }

#5.
nro1 = 6
nro2 = 2
suma = nro1 + nro2
resta = nro1 - nro2
multiplicacion = nro1 * nro2
division = nro1 / nro2
print(f"La suma de los numeros es: {suma}\nLa resta de los numeros es: {resta}\nLa multiplicación de los numeros es:{multiplicacion}\nLa división de los numeros es: {division}")

#En Java
#public class EjercicioClase1 {
#    public static void main(String[] arg) {
#        int suma, resta, multiplicacion;
#        float division;
#        int num1 = 6;
#        int num2 = 2;
#        suma = num1 + num2;
#        resta = num1 - num2;
#        multiplicacion = num1 * num2;
#        division = num1 / num2;
#        
#        System.out.printf("Los resultados son: suma = %d, resta = %d, multiplicacion = %d, division = %f", suma, resta, multiplicacion, division);
#        
#    }
#}
