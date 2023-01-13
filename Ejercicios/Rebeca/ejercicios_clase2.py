#Consigna 1) Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

Materias=['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
#print(Materias)


#Consigna 2) Con el programa anterior, utilice todos los metodos vistos en clases, mostrando cada uno con un print. 
#Metodo 1
Materias.append(2)
print(Materias)

#Metodo 2
#print(len(Materias))

#Metodo 3
#Materias.pop(2)
#Materias.pop()
#print(Materias)

#Metodo 4
#Materias.append('Historia')
#print(Materias)
#print(Materias.count('Historia')) 

#Metodo 5
#print(Materias.index("Lengua"))

#Consigna3) Escribir un programa que almacene una lista de ingredientes para hacer galletas y convierta dicha lista en una tupla.

Receta=['harina','azúcar','banana','leche']
#print(Receta)
Receta2=tuple(Receta)
#print(Receta2)




#--------------------------------------------equivalente en JAVA------------------------------------------------------


#Consigna 1) Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
'''
public class Main{
    public static void main(String[] args) {
        
       /* String[] Materias=new String[5];
        Materias[0]="Matemáticas";
        Materias[1]="Física";
        Materias[2]="Química";
        Materias[3]="Historia";
        Materias[4]="Lengua";
       */
       String[] Materias={"Matemáticas","Física","Química","Historia","Lengua"};
        for(int i=0; i<5; i++){
           System.out.println(Materias[i]);  
        }
    }
}

'''

#Consigna 2) Con el programa anterior, utilice todos los metodos vistos en clases, mostrando cada uno con un print. 
#Metodo 1: Usando el objeto ArrayList podemos añadir un objeto en una posición determinada, que es el orden en se insertan en la lista. Para ello usaremos el método añadir al final ( .add).
# Método 2: Luego usaremos un método para obtener el número de objetos en la lista (.size).
#Método 3: Para eliminar un elemento de un ArrayList nos vamos a apoyar en el método .remove(), el cual espera como parámetro el índice del elemento que queremos eliminar. Recordar que los índices de un elemento ArrayList empiezan a enumerarse por el valor 0.
#Metodo 4: 
#Metodo 5: 





'''
import java.util.ArrayList; 

public class Main { 
 public static void main (String [ ] Args) { 
 ArrayList <String> Materias = new ArrayList<String> (); // creación del objeto
 Materias.add ("Matemáticas"); 
 Materias.add ("Física"); 
 Materias.add ("Química"); 
 Materias.add ("Historia"); 
 Materias.add ("Lengua"); 
 int i = 0; 
 System.out.println ("Las materias son: "); 
 for (String nombre : Materias) { 
     System.out.println ((i) + ".- " +nombre); 
 i++; } 
 
int tamanio = Materias.size();
System.out.println("Actualmente el número de elementos es de "+tamanio);

System.out.println("Tras eliminar el elemento de la posición 2, la lista queda así. Obeservar que los elementos toman nuevas posiciones...");
Materias.remove(2);
int j=0;
for (String nombre : Materias) { 
     System.out.println ((j) + ".- " +nombre); 
 j++; } 
 } } 

'''

#Consigna3) Escribir un programa que almacene una lista de ingredientes para hacer galletas y convierta dicha lista en una tupla.

#ver: https://lineadecodigo.com/java/convertir-un-array-en-una-lista/