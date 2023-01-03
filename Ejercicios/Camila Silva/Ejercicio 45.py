# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 

### Crea un bucle while con las siguientes características:
#  1. El valor inicial de la variable x será de 0.
#  2. El valor de incremento será 1.
#  3. La condición de salida del bucle será mayor o igual a 30.
#  4. La ejecución se deberá romper cuando x valga 15.
#  5. Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#  6. Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#  7. En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
#  8. Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x.
x = 0
while x < 30:
    x += 1
    if x == 15:
      print('Se rompió la ejecución del bucle cuando x valía '+ str(x))
      break
    elif (x == 4) or (x == 6) or (x == 10):
      print('Se saltó el valor ' + str(x) + ' de x')
      continue
    else:
     print('El valor del bucle es: ' + str(x) ) 
   

### Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100.

for i in range(7,701,100):
 print(i)
### Basta con que imprimas el valor de cada iteración
# En Java seria:
# public class EjercicioForRange {
#     public static void main(String args[]) {
#       for (Integer i = 7; i <= 700; i += 100)
#     System.out.println(i);
#     }
# }