# 1. Solicitar al usuario que ingrese su dirección email. 
# Imprimir un mensaje indicando si la dirección es válida o no, 
# valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".
def email(correo):
     if '@' in correo:
         print("El correo es valido")
     else:
         print("El correo es invalido")

correo= input("Bienvenido. Ingrese su correo electronico:")
email(correo)

# 2. Escribir una función que, dado un número de DNI, 
# retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos
def DNI(DNIUser):
    if len(DNIUser)==7 or len(DNIUser)==8:
        print("El DNI ingresado es valido")
    else:
        print("DNI ingresado es invalido")

DNIUser=(input("Ingrese su DNI:"))
DNI(DNIUser)

#JAVA
# def saludos(nombre):
#      #nombre = input("Ingrese su nombre")
#      saludando = print("Hola" + nombre + " como estas?")
#      return saludando
# nombre = input("Ingrese su nombre")
# saludos(nombre)
# public class Saludo {
#   public static void main(String[] args) {
#     String nombre;
#     System.out.print("Ingrese su nombre: ");
#     nombre = System.console().readLine();
#     System.out.println("Hola " + nombre + " "+ "como estas");
#   }
# }