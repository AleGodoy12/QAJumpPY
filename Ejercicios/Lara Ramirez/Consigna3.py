#Crea un bucle while con las siguientes características:
#El valor inicial de la variable x será de 0.
#El valor de incremento será 1.
#La condición de salida del bucle será mayor o igual a 30.
#La ejecución se deberá romper cuando x valga 15.
#Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
#Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle 
# cuando x valía ' + x.

#Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100.
#Basta con que imprimas el valor de cada iteración


### EJERCICIO 1

x = 0
while x <= 30:
 print ('El valor del bucle es', x)
 x +=1
 if x == 4:
    pass
    print ('Se saltó el valor ', x, ' de x')
 elif x == 6:
    pass
    print ('Se saltó el valor ', x, ' de x')
 elif x == 10:
  pass
  print ('Se saltó el valor ', x, ' de x')
 if x == 15:
  break
print ('Se rompió la ejecución del bucle cuando valía ', x)

### EJERCICIO 2

i = 7
for i in range(7, 800, 100):
 print (i)