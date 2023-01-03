
# 1. Escribir un programa que almacene las asignaturas 
# de un curso (por ejemplo Matemáticas, Física,
#  Química, Historia y Lengua) en una lista y la
#  muestre por pantalla.

Asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(Asignaturas)


# import java.util.List;
# import java.util.ArrayList;

# class Listas {
#     public static void main(String[] args) {
#         List<String> lista = new ArrayList<>();
#         lista.add("Matematicas");
#         lista.add("Fisica");
#         lista.add("Quimica");
#         lista.add("Historia");
#         lista.add("Lengua");
#         System.out.println(lista);
        
#     }
# }

# 2. Con el programa anterior, 
# utilice todos los metodos vistos en clases,
#  mostrando cada uno con un print. 

Asignaturas.append("Matemáticas")
print(Asignaturas)


print(len(Asignaturas))

Asignaturas.pop(2)
print(Asignaturas)

print(Asignaturas.count("Matemáticas"))

print(Asignaturas.index("Física"))

# En Java seria:
# import java.util.List;
# import java.util.ArrayList;
# class Listas {
#     public static void main(String[] args) {
#         List<String> lista = new ArrayList<>();
#         lista.add("Matematicas");
#         lista.add("Fisica");
#         lista.add("Quimica");
#         lista.add("Historia");
#         lista.add("Lengua");
#         System.out.println(lista + "\n ");
        
#         lista.add("Geografia");
#         System.out.println("Agregamos Geografia a la lista \n " + lista + "\n ");
        
#         System.out.println("La cantidad de elementos es " + lista.size() + "\n ");
         
#         // Contar ocurrencias de una lista  
#         String coincidencia = "Fisica";
#         int contador = 0;
#         for(int i = 0;  i < lista.size();  i++)   
#         {
#         if (lista.get(i) == coincidencia) {
#         contador = contador + 1;}
#         }
#      if(contador == 0) {
#       System.out.println("No logramos encontrarlo en la lista" + "\n ");
#     } else {
#       System.out.println("La cantidad de ocurrencias es " + contador + "\n ");
#     }
#          System.out.println("El elemento en la pos 0 es " + lista.get(0) + "\n ");
#         lista.remove(0);
#         System.out.println("Eliminamos el elemento en la pos 0 \n  " +lista);
#     }
# }


# 3. Escribir un programa que almacene una lista de ingredientes para hacer galletas y convierta dicha lista en una tupla.

Ingredientes = ["Azucar", "Huevos", "Harina", "Manteca", "Chispas de Chocolate", "Polvo de hornear"]
print(tuple(Ingredientes))

# En Java pasariamos de Tupla a Lista de esta forma:
# import org.javatuples.*;
# import java.util.List;  
# class Tuplas {
#     public static void main(String[] args) {
#        Quintet <String, String, String, String, String> quinteto = new Quintet<String, String, String, String, String>
#  ("Huevos", "Azucar", "Harina", "Leche", "Chispas de chocolate");  
#  List<Object> resultado = quinteto.toList();  
# System.out.println(resultado);  
#     }
# }