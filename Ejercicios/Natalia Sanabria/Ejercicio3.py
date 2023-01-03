#3
# ### Crea un bucle while con las siguientes características:
#  1. El valor inicial de la variable x será de 0.
#  2. El valor de incremento será 1.
#  3. La condición de salida del bucle será mayor o igual a 30.
#  4. La ejecución se deberá romper cuando x valga 15.
#  5. Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#  6. Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#  7. En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
#  8. Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x.
x=0;
while x<=30:
    x+=1;
    print ('El valor del bucle es: ' , x);
    if x==4 or x==6 or x==10:
        print('Se saltó el valor ' , x ,'de x');
        continue;
    if x==15:
        print('Se rompió la ejecución del bucle cuando x valía ' ,x);
        break;

# ### Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100.
# ### Basta con que imprimas el valor de cada iteración
for i in range(7,800,100):
     print(i);
# En Java:
# for (Integer i = 7; i < 800; i+100 ) {
#     System.out.println(i);
# }