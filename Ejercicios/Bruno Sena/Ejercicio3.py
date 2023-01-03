### Crea un bucle while con las siguientes características:
#  1. El valor inicial de la variable x será de 0.
#  2. El valor de incremento será 1.
#  3. La condición de salida del bucle será mayor o igual a 30.
#  4. La ejecución se deberá romper cuando x valga 15.
#  5. Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#  6. Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#  7. En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
#  8. Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x.

"""
Primer ejercicio
"""
x = 0 #Primero asigno a la variable "x" un valor de cero
while x <= 30: #Luego inicio el bucle while indicando la condicional de que x debe ser menor o igual a 30 para que pueda ejecutarse
    x += 1 #Luego incremento la variable x en 1 con cada ejecución
    if x == 4 or x == 6 or x == 10: #Hago otra condicional la cual menciona que si x es igual a 4 o 6 o 10 entonces ejecute tal acción
        print('Se saltó el valor ', x, ' de x') #La acción sería mostrar el mensaje que se saltó el valor
        continue #Continuo con la ejecución
    elif x == 15: #Otra condicional la cual indica que si x es igual a 15 entonces ejecute tal acción
        print('Se rompió la ejecución del bucle cuando x valía ', x) #Imprime en pantalla que se rompió la ejecución del bucle 
        break #Finaliza el bucle antes de que x pueda llegar a 30
    else: #Si no se cumplen las condicionales anteriores entonces ejecuta esto
        print('El valor del bucle es: ', x) #Muestro por pantalla un mensaje que diga el valor actual de la variable x

### Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100.
### Basta con que imprimas el valor de cada iteración

"""
Segundo ejercicio
"""
for valor in range(7, 700, 100): #Le indico al bucle for que nuestro valor incial es 7 dentro de range(valor inicial, parar, paso)
    print("El valor actual es: ", valor) #Muestra un mensaje según el número de ejecuciones y muestra el valor actual de la variable valor