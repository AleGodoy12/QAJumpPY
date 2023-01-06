# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 
# Recorda investigar y comentar la resolucion en java

#1. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturasDelCurso = ['Matematicas', 'fisica', 'quimica', 'historia', 'lengua']
print(asignaturasDelCurso)

#-----------------------------------------------------------------------------------------------------
#import java.util.*;

#public class NewClass {
    #public static void main(String[] args) {
    
       # String asignaturasDelCurso[] = {"Matematicas", "fisica", "quimica", "historia", "lengua"};
       # System.out.println(Arrays.toString(asignaturasDelCurso));
        
    #}   
#} 
# ----------------------------------------------------------------------------------------------------
        #finalmente usamos un array list porque los string en java no se pueden modificar.

#ArrayList<String> asignaturasDelCurso = new ArrayList<String>();
#asignaturasDelCurso.add("Matematicas");
#asignaturasDelCurso.add("fisica");
#asignaturasDelCurso.add("quimica");
#asignaturasDelCurso.add("historia");
#asignaturasDelCurso.add("lengua");
#for(int i = 0;i < asignaturaDelCurso.size(); i++){
#    System.out.println(asignaturasDelCurso.get(i));
# }


#2. Con el programa anterior, utilice todos los metodos vistos en clases, mostrando cada uno con un print. 

print(asignaturasDelCurso[0])
#System.out.println(asignaturasDelCurso.get(0));

print(asignaturasDelCurso[-1]) 
#System.out.println(asignaturasDelCurso.get(asignaturasDelCurso.size() -1));
# ponemos el -1  porque usamos el metodo size y este empieza en 1 y no desde 0.

print(asignaturasDelCurso[-2:])  #Devuelve ['historia', 'lengua']

asignaturasDelCurso += ['cs. naturales', 'cs. sociales']
#asignaturasDelCurso.add("cs. naturales");
#asignaturasDelCurso.add("cs. sociales");


asignaturasDelCurso[2] = 'ingles' #cambio la asignatura  quimica por  ingles
print(asignaturasDelCurso)
#asignaturasDelCurso.set(2, "ingles");


asignaturasDelCurso[:3]= ['italiano','frances']
print(asignaturasDelCurso)       #Devuelve ['italiano', 'frances', 'historia', 'lengua'] inserta delante de la tercera posicion

asignaturasDelCurso[:3] = [ ]
print(asignaturasDelCurso)   # devuelve ['historia', 'lengua']
#List<String> lista = asignaturasDelCurso.subList(0, 3);
#lista.clear();

asignaturasDelCurso = [  ]
print(asignaturasDelCurso)  # borra todo
#asignaturasDelCurso.clear();


asignaturasDelCurso = ['Matematicas', 'fisica', 'quimica', 'historia', 'lengua','fisica'] #La creo nuevamente porque borramos la lista
asignaturasDelCurso.append("plastica")
print(asignaturasDelCurso)
#asignaturasDelCurso.add("plastica");

print(len(asignaturasDelCurso)) 
#System.out.println(asignaturasDelCurso.size()); 


asignaturasDelCurso.pop()
print(asignaturasDelCurso)
#asignaturasDelCurso.remove(0);


asignaturasDelCurso.pop(1)
print(asignaturasDelCurso)    #devuelve ['Matematicas', 'quimica', 'historia', 'lengua', 'fisica']
#asignaturasDelCurso.remove(1);

print(asignaturasDelCurso.count('fisica'))
#System.out.println(Collections.frequency(asignaturasDelCurso, "fisica"));

print(asignaturasDelCurso.index('matematica'))
#asignaturasDelCurso.indexOf("matematica");


#3. Escribir un programa que almacene una lista de ingredientes para hacer galletas y convierta dicha lista en una tupla.

ingredientesGalletas = ['harina','azucar','huevo','leche','limon']
print(tuple(ingredientesGalletas))

#pendiente,no lo comprendi del todo.