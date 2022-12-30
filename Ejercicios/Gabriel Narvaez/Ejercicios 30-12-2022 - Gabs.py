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


### Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100.
### Basta con que imprimas el valor de cada iteración

#Ejercicio 1)
x = 0
while x <=30:
    x+=1
    if x == 4 or x == 6 or x == 10:
        print(f'Se saltó el valor de {x} de "x"')
        continue
    elif x == 15:
        print(f'Se rompió la ejecución del bucle cuando "x" valía {x}')
        break
    else:
        print(f'El valor del bucle es: {x}')

#Ejercicio 2)        
for i in range(7,700,100):
    print(i)

#------------------------------
# Investigación ejercicios Java
#------------------------------

#Ejercicio 2)    

# class Main {
#     public static void main(String[] args) {
#         for (int i = 7; i < 700; i += 100) {
#             System.out.println(i);
#         }
#     }
# }