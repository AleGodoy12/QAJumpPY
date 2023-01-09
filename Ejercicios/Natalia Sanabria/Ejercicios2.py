#1
asignaturas_lista=["Matemáticas", "Física", "Química", "Historia","Lengua"];
print(asignaturas_lista);
#Java:
# package lista; 
# public class asignaturas_lista{
#     public class void main(String[] args){
#         List<String> asignaturas = new ArrayList<> ();
#         asignaturas.add("Matemáticas");
#         asignaturas.add("Física");
#         asignaturas.add("Química");
#         asignaturas.add("Historia");
#         asignaturas.add("Lengua");
#        System.out.println(asignaturas.get(0));
#        System.out.println(asignaturas.get(1));
#        System.out.println(asignaturas.get(2));
#        System.out.println(asignaturas.get(3));
#        System.out.println(asignaturas.get(4));
#     }
# }

#2
#Lo paso a tupla
asignaturas_tupla=("Matemáticas", "Física", "Química", "Historia","Lengua");
print(asignaturas_tupla);
#Java:
# package arreglos;
# public class arreglos{
#     public static void main(String[] arg){
#         String [] asignaturas= new String [4];
#         asignaturas=["Matemáticas"];
#         asignaturas=["Física"];
#         asignaturas=["Química"];
#         asignaturas=["Historia"];
#         asignaturas=["Lengua"];
#         System.out.println(asignaturas.get(0));
#         System.out.println(asignaturas.get(1));
#         System.out.println(asignaturas.get(2));
#         System.out.println(asignaturas.get(3));
#         System.out.println(asignaturas.get(4));

#     }
# }

#Agrego materia nueva al comienzo de la lista
asignaturas_lista=["Matemáticas", "Física", "Química", "Historia","Lengua"];
asignaturas_lista[:0]=["Arte"];
print(asignaturas_lista);
#Java:
# package lista; 
# public class asignaturas_lista{
#     public class void main(String[] args){
#         List<String> asignaturas = new ArrayList<> ();
#         asignaturas.add("Arte");
#         asignaturas.add("Matemáticas");
#         asignaturas.add("Física");
#         asignaturas.add("Química");
#         asignaturas.add("Historia");
#         asignaturas.add("Lengua");
#        
#        System.out.println(asignaturas.get(0));
#        System.out.println(asignaturas.get(1));
#        System.out.println(asignaturas.get(2));
#        System.out.println(asignaturas.get(3));
#        System.out.println(asignaturas.get(4));
#        System.out.println(asignaturas.get(5));
#     }
# }



#Elimino las primeras 3 materias de la lista
asignaturas_lista=["Matemáticas", "Física", "Química", "Historia","Lengua"];
asignaturas_lista[:3]=[];
print(asignaturas_lista);
#Java:
# package lista; 
# public class asignaturas_lista{
#     public class void main(String[] args){
#         List<String> asignaturas = new ArrayList<> ();
#         asignaturas.add("Matemáticas");
#         asignaturas.add("Física");
#         asignaturas.add("Química");
#         asignaturas.add("Historia");
#         asignaturas.add("Lengua");
#         asignaturas.remove(3);
#        System.out.println(asignaturas.get());
#     }
# }

#APPEND
asignaturas_lista=["Matemáticas", "Física", "Química", "Historia","Lengua"];
asignaturas_lista.append("Biologia");
print(asignaturas_lista);

#Tamaño de la lista
asignaturas_lista=["Matemáticas", "Física", "Química", "Historia","Lengua"];
print (len(asignaturas_lista));
#Java:
# package lista; 
# public class asignaturas_lista{
#     public class void main(String[] args){
#         List<String> asignaturas = new ArrayList<> ();
#         asignaturas.add("Matemáticas");
#         asignaturas.add("Física");
#         asignaturas.add("Química");
#         asignaturas.add("Historia");
#         asignaturas.add("Lengua");
#        System.out.println(asignaturas.size());
#     }
# }

#POP
asignaturas_lista=["Matemáticas", "Física", "Química", "Historia","Lengua"];
asignaturas_lista.pop();
print(asignaturas_lista);

#COUNT
asignaturas_lista=["Lengua","Matemáticas", "Física", "Química", "Historia","Lengua","Lengua"];
print(asignaturas_lista.count("Lengua"));

#INDEX
asignaturas_lista=["Matemáticas", "Física", "Química", "Historia","Lengua"];
print(asignaturas_lista.index("Historia"));

#len,index,count tambien se pueden usar en tuplas, pero no POP,COUNT o Append, ya que las tuplas no pueden alterarse.


#3
lista_galletas= ["Harina","Mantequilla","Azucar","Bicarbonato","Esencia de vainilla"];
print(lista_galletas);
tuple(lista_galletas);
print(tuple(lista_galletas));
# #Java:
# import java.util.ArrayList;
# import java.util.List;
# public class listaaarray{
#     public static void main(String[] args){
#         List<String> lista_galletas= new ArrayList<> ();

#         #lista
#         lista_galletas.add("Harina");
#         lista_galletas.add("Mantequilla");
#         lista_galletas.add("Azucar");
#         lista_galletas.add("Bicarbonato");
#         lista_galletas.add("Esencia de vainilla");
#         System.out.println(lista_galletas.size());
#         System.out.println(lista_galletas);

#         #tupla
#         String[] galletas= new String[lista_galletas.size()];
#         galletas.toArray(lista_galletas);
#         System.out.println(galletas.get(0));
#         System.out.println(galletas.get(1));
#         System.out.println(galletas.get(2));
#         System.out.println(galletas.get(3));
#         System.out.println(galletas.get(4));
#     }
# }


