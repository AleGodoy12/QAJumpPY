# Agregar un archivo .py en la carpeta con tu nombre con la resolucion de cada una de las consignas. 


#1. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por 
#una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está 
#en el diccionario debe mostrar un mensaje informando de ello.

preciosDeLasFrutas={'naranja':100,'manzana':240,'banana':210,'ciruela':250}
fruta=input("Ingrese la fruta a comprar:")
kilos=int(input("Ingrese cuantos kilos va a comprar:"))

if fruta.lower() in preciosDeLasFrutas:
    precio=(kilos*preciosDeLasFrutas[fruta.lower()])
    print("El kilo de ",fruta,"esta a",preciosDeLasFrutas[fruta.lower()])
    print("total:", precio)
else:
    print("La fruta no esta en la lista")

#2. Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 
#6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato 
#<asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> 
#son sus créditos. Al final debe mostrar también el número total de créditos del curso.

asignaturas={'Matematicas':6,'Fisica':4,'Quimica':5}
totalCredito=0
for i in asignaturas:
    totalCredito +=asignaturas[i]
    print (i,"tiene",(asignaturas[i]),"creditos")
print("Total  creditos:", totalCredito)
    
#3. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras 
#en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa 
#debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el 
#diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

print("###Por favor ingrese las palabra que desee agregar seguido de : y su traduccion")
palabras= input( "si ingresa  mas de una palabra separelo con una coma etc###\n")
listaTraduccion= palabras.split(",") #El split transforma en lista y separa por la coma
dicTraducido= {} # Creo un diccionario para poder cargar los valores que ingresamos
for i in listaTraduccion:
    listaTraduccion= i.split(":") #El split transforma en lista y separa por los dos puntos
    dicTraducido[listaTraduccion[0].lower()]= listaTraduccion[1].lower() # ingreso los valores de la lista al diccionario

print("_____________________________________________")
print("la lista de palabras en ingles son:") #Lista las claves de los valores ingresados  para poder elegir 
for i in dicTraducido.keys():
    print("-",i)
print("_____________________________________________")
palabraIngresada= input("escriba la palabra que desea traducir:\n")
if palabraIngresada.lower() in dicTraducido:
    print("La palabra",palabraIngresada.lower(),"en ingles es",dicTraducido[palabraIngresada.lower()])
else:
    print("No tenemos esa palabra en el diccionario")

#______________________________________________________________________________________________________________
# Agregar en JAVA los ejercicios hechos en clase.
#public static void main(String[] args) {

#    HashMap<String,Character> listaDivisas = new HashMap<String,Character>();
#    String nombreDivisa;
#    Character divisa;

#    System.out.println("Introduce el nombre de la divisa:");
#        nombreDivisa = sc.next();
#       System.out.println("Introduce el simboo de la divisa:");
#        divisa = sc.nextCharacter();
#       if (listaDivisas.containsKey(nombreDivisa)) {
#            System.out.println("No se puede introducir el nombre de la divisa. Ya se encuentra en la lista.");
#        } else {
#            listaDivisas.put(nombreDivisa, divisa);               
#        }

#    Iterator<String> divisasNuevas = listaDivisas.keySet().iterator();
#    System.out.println("Estan las siguientes divisas:");
#    while(divisasNuevas.hasNext()){
#        nombre = divisasNuevas.next();
#        System.out.println(nombre + " - " + listaDivisas.get(nombre));
#    }

#}
            