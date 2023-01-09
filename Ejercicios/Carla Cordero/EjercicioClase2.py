#1.
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print("Las materias son:",materias)

#En Java
# import java.util.List;
# import java.util.ArrayList;
#
# class Materias {
#     public static void main(String[] args) {
#         List<String> Materias = new ArrayList<>();
#         Materias.add("Matematicas");
#         Materias.add("Fisica");
#         Materias.add("Quimica");
#         Materias.add("Historia");
#         Materias.add("Lengua");
#         System.out.println(Materias);
#        
#     }
# }

#2.
#append
materias.append("Educación Física")
print(materias)
#pop
materias.pop(0)
print(materias)
#count
print(materias.count("Lengua"))
#len
print(len(materias))
#index
print(materias.index("Física"))

#3.
ingredientes = ["Azúcar", "Harina", " Huevos" , "Escencia de vainilla" , "Manteca"]
print ("La lista de ingredientes es:",ingredientes)
listaAtupla = tuple(ingredientes)
print("La lista convertida a tupla es:",listaAtupla)