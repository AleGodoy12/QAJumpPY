# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 
# Recorda investigar y comentar la resolucion en java

#1. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'lengua', 'ciencias sociales']
print(asignaturas)

#2. Con el programa anterior, utilice todos los metodos vistos en clases, mostrando cada uno con un print. 

#Metodos clase 1)
print(asignaturas[0].upper())
print(asignaturas[1].lower())
print(asignaturas[-2].capitalize())
print(asignaturas[0].count('i'))
print(asignaturas[0].isdigit())
print(asignaturas[0].isalnum())
print(asignaturas[0].isalpha())
print(asignaturas[-1].islower())
print(asignaturas[0].isupper())
print(asignaturas[0].istitle())
print(asignaturas[0].isdigit())
print(asignaturas[0].startswith('Mat'))
print(asignaturas[0].endswith('s'))
print(asignaturas[0].replace('e', '3'))

#metodos clase 2)
letras = ['a','b','c','d']
asignaturas_letras = asignaturas + letras
print(asignaturas_letras)

asignaturas_letras[-1] = 'z'
print(asignaturas_letras)

asignaturas_letras[6:] = []
print(asignaturas_letras)

asignaturas_letras[:6] += letras
print(asignaturas_letras)

asignaturas_letras.append('f')
print(asignaturas_letras)

asignaturas_letras.pop()
print(asignaturas_letras)

asignaturas_letras.pop(-4)
print(asignaturas_letras)

print(asignaturas_letras.index('ciencias sociales'))
print(asignaturas_letras[5].count('i'))
print(len(asignaturas_letras))
print(len(asignaturas_letras[5]))

nuevasLetras = ('j','k')
asignaturas_letras.append(nuevasLetras)
print(asignaturas_letras)

#3. Escribir un programa que almacene una lista de ingredientes para hacer galletas y convierta dicha lista en una tupla.
ingredientesGalletas = ['Harina','Agua','Azucar','Chocolate']
print(type(ingredientesGalletas))
ingredientesGalletas = tuple(ingredientesGalletas)
print(type(ingredientesGalletas))

#------------------------------
# Investigación ejercicios Java
#------------------------------

# Ejercicio 1)

# import java.util.*;  
# public class Main{  
#     public static void main(String args[]){  
#         List<String> asignaturas=new ArrayList<String>();  
#         asignaturas.add("Matematicas");  
#         asignaturas.add("Fisica");  
#         asignaturas.add("Quimica");  
#         asignaturas.add("Historia");
#         asignaturas.add("lengua"); 
#         asignaturas.add("ciencias sociales"); 
#         System.out.println(asignaturas.get(0)); 
#         System.out.println(asignaturas.get(1)); 
#         System.out.println(asignaturas.get(2)); 
#         System.out.println(asignaturas.get(3)); 
#         System.out.println(asignaturas.get(5)); 
#     }  
# }  

#Ejercicio 2)
# import java.util.*;  
# public class Main{  
#     public static void main(String args[]){  
#         List<String> letras=new ArrayList<String>();
#         List<String> asignaturas=new ArrayList<String>();
#         List<String> asignaturas_letras=new ArrayList<String>();

#         letras.add("a");  
#         letras.add("b");  
#         letras.add("c");  
#         letras.add("d");
#         asignaturas.add("Matematicas");  
#         asignaturas.add("Fisica");  
#         asignaturas.add("Quimica");  
#         asignaturas.add("Historia");
#         asignaturas.add("lengua"); 
#         asignaturas.add("ciencias sociales");
#         asignaturas_letras.addAll(letras);
#         asignaturas_letras.addAll(asignaturas);

#         System.out.println(asignaturas_letras);

#         asignaturas_letras.set(asignaturas_letras.size()-1, "z");
#         System.out.println(asignaturas_letras.get(asignaturas_letras.size()-1));

#         System.out.println(asignaturas_letras.subList(0,6));
#         System.out.println(asignaturas_letras.subList(6, asignaturas_letras.size()));
         
#         asignaturas_letras.remove(1);
#         System.out.println(asignaturas_letras);

#         asignaturas_letras.clear();
#         System.out.println(asignaturas_letras);

#         asignaturas_letras.add(2,"nuevo");
#         System.out.println(asignaturas_letras);

#         asignaturas_letras.add(asignaturas_letras.size(),"z");
#         System.out.println(asignaturas_letras);

#         System.out.println(asignaturas_letras.indexOf("ciencias sociales"));

#         String test = "Hola mundoo";
#         int contador = 0;

#         for (int i = 0; i < test.length(); i++) {
#           if (test.charAt(i) == 'o') {
#              contador++;
#              }
#          }
#          System.out.println(contador);


#         EJERCICIO 3)
#         ------------
#          List<String> ingredientesGalletas = Arrays.asList("Harina", "Agua", "Azucar", "Chocolate");
#          System.out.println(ingredientesGalletas);

#     }  
# }  