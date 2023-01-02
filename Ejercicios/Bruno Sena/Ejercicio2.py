# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 
# Recorda investigar y comentar la resolucion en java

#1. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua", "Biologia"]
print(asignaturas);

"""
Solución Java:

public class Asignaturas {
    public static void main(String[] args) {
        String[] asignaturas = {"Matemáticas", "Física", "Química", "Historia", "Lengua", "Biologia"};

        System.out.println(asignaturas[0]);
        System.out.println(asignaturas[1]);
        System.out.println(asignaturas[2]);
        System.out.println(asignaturas[3]);
        System.out.println(asignaturas[4]);
        System.out.println(asignaturas[5]);
    }
}
"""

#2. Con el programa anterior, utilice todos los metodos vistos en clases, mostrando cada uno con un print. 
print(asignaturas[0])
print(asignaturas[-1])
print(asignaturas[:4])
print(asignaturas[-3:])
asignaturas += ["Literatura", "Inglés", "Portugués"]
print(asignaturas)
asignaturas[2] = "Química avanzada"
print(asignaturas)
asignaturas[:3]= [ ]
print(asignaturas)
asignaturas = [ ]
print(asignaturas)
asignaturas.append("Literatura")
print(asignaturas)
asignaturas.extend(["Biologia", "Biologia", "Biologia", "Historia", "Geografía", "Química"])
print(len(asignaturas))
print(asignaturas)
asignaturas.pop(0)
print(asignaturas)
print(asignaturas.count("Biologia"))
print(asignaturas.index("Química"))

"""
Solución Java:

public class Asignaturas {
    public static void main(String[] args) {
        List<String> asignaturas = new ArrayList<>(Arrays.asList("Matemáticas", "Física", "Química", "Historia", "Lengua", "Biología"));
    	
    	String primerElemento = asignaturas.get(0);
    	String ultimoElemento = asignaturas.get(asignaturas.size() -1);
    	int tamanioAsignatura = asignaturas.size();
    	List<String> primerosCuatro = asignaturas.subList(0, 4);
    	List<String> ultimosTres = asignaturas.subList(tamanioAsignatura - 3, tamanioAsignatura);
    	System.out.println(primerElemento);
    	System.out.println(ultimoElemento);
    	System.out.println(primerosCuatro);
    	System.out.println(ultimosTres);
    	asignaturas.add("Literatura");
    	asignaturas.add("Inglés");
    	asignaturas.add("Portugués");
    	System.out.println(asignaturas);
    	asignaturas.set(2, "Química avanzada");
    	System.out.println(asignaturas);
    	List<String> eliminarTres = asignaturas.subList(0, 3);
    	eliminarTres.clear();
    	System.out.println(asignaturas);
    	asignaturas.clear();
    	System.out.println(asignaturas);
    	asignaturas.add("Literatura");
    	System.out.println(asignaturas);
    	List<String> otrasAsignaturas = new ArrayList<>(Arrays.asList("Biologia", "Biologia", "Biologia", "Historia", "Geografía", "Química"));
    	asignaturas.addAll(otrasAsignaturas);
    	System.out.println(asignaturas.size());
    	System.out.println(asignaturas);
    	asignaturas.remove(0);
    	System.out.println(asignaturas);
    	int countBiologia = Collections.frequency(asignaturas, "Biologia");
    	System.out.println(countBiologia);
    	System.out.println(asignaturas.indexOf("Química"));

    }
}
"""


#3. Escribir un programa que almacene una lista de ingredientes para hacer galletas y convierta dicha lista en una tupla.
ingredientes = ["Harina", "Azúcar", "Huevos", "Mantequilla"]
print(tuple(ingredientes))

"""
Solución Java:

public class Asignaturas {
    public static void main(String[] args) {
        String[] ingredientes = {"Harina", "Azúcar", "Huevos", "Mantequilla"};
    	List<String> listaIngredientes = Arrays.asList(ingredientes);
    	List<String> tuplaIngredientes = Collections.unmodifiableList(listaIngredientes);
    	System.out.println(tuplaIngredientes);
    }
}
"""
