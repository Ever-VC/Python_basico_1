'''
Las tuplas y los diccionarios pueden trabajar juntos
Se ha preparado un ejemplo sencillo, mostrando como las tuplas y los 
diccionarios pueden trabajar juntos.

Imaginemos el siguiente problema:

*   necesitas un programa para calcular los promedios de tus alumnos;
*   el programa pide el nombre del alumno seguido de su calificación; los 
    nombres son ingresados en cualquier orden;
    el ingresar un nombre vacío finaliza el ingreso de los datos (Nota 1: 
    ingresar una puntuación vacía generará la excepción ValueError, pero no te preocupes por eso 
    ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el segundo parte de 
    la serie del curso Fundamentos de Python)
*   una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.

Observa el código en el editor, se muestra la solución.
'''

school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break

    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
	    break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

'''

Crrando copias de rebanadas de listas:

# Esto tiene formato de código
[ ]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
[4, 2]
Econtrar la posición de un elemento dado dentro de una lista

[ ]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")
Elemento encontrado en el índice 4
Eliminando valores repetidos dentro de una lista

[ ]
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for value in my_list:
    if value not in new_list:
      new_list.append(value)


print("La lista con elementos únicos:")
print(new_list)
La lista con elementos únicos:
[1, 2, 4, 6, 9]
SECUENCIA DE FIBONACCI - APLICANDO RECURSIVIDAD
¿Estás familiarizado con la serie Fibonacci?

Son una secuencia de números enteros los cuales siguen una regla sencilla:

el primer elemento de la secuencia es igual a uno (Fib1 = 1)
el segundo elemento también es igual a uno (Fib2 = 1)
cada número después de ellos son la suman de los dos números anteriores (Fibi = Fibi-1 + Fibi-2)
Aquí están algunos de los primeros números en la serie Fibonacci:

fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13
¿Que opinas acerca de implementarlo como una función?

Creemos nuestra propia función fib y probémosla, aquí esta:

[ ]
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


for n in range(1, 11): # probando
    print(n, "->", fib(n))
1 -> 1
2 -> 1
3 -> 2
4 -> 3
5 -> 5
6 -> 8
7 -> 13
8 -> 21
9 -> 34
10 -> 55
FACTORIAL DE UN NUMERO - APLICANDO RECURSIVIDAD
n! = 1 × 2 × 3 × ... × n-1 × n

Es obvio que:

1 × 2 × 3 × ... × n-1 = (n-1)!

Entonces, finalmente, el resultado es:

n! = (n-1)! × n

Esto se empleará en nuestra nueva solución.

[63]
4 s
def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial(n - 1)

print("Ingrese el numero del cual desea saber su factorial")
num = int(input(": "))
print("El factorial de [", num, "] es: ", factorial(num))
Ingrese el numero del cual desea saber su factorial
: 4
El factorial de [ 4 ] es:  24
Tuplas

[ ]
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)
(2,) (3, 123) (1,)
Diccionarios

[ ]
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary['cat'])
print(phone_numbers['Suzy'])
[ ]
pol_esp_dictionary = {
    "kwiat": "flor",
    "woda": "agua",
    "gleba": "tierra"
    }

item_1 = pol_esp_dictionary["gleba"] # Ejemplo 1
print(item_1) # salida: tierra

item_2 = pol_esp_dictionary.get("woda") # Ejemplo 2
print(item_2) # salida: agua
[ ]
dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")
gato no está en el diccionario
león no está en el diccionario
caballo -> cheval
Diccionarios con formato vertical o sangría francesa

[ ]
# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
}
# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
              'Suzy': 22657854310
}
Recorriendo diccionarios

[ ]
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
[64]
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }

for item in pol_esp_dictionary:
    print(pol_esp_dictionary[item])
[ ]
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)
[ ]
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for french in dictionary.values():
    print(french)
Ordenando un diccionario

[ ]
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
for key in sorted(dictionary.keys()):
  print(key)
caballo
gato
perro
Modificar diccionarios

[ ]
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['gato'] = 'minou'
print(dictionary)
Agregando nuevas claves

[ ]
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['cisne'] = 'cygne'
print(dictionary)
[ ]
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary.update({"pato": "canard"})
print(dictionary)
Eliminando una clave

[ ]
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

del dictionary['perro']
print(dictionary)
Elimina la ultima clave

[ ]
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary.popitem()
print(dictionary) # salida: {'gato': 'chat', 'perro': 'chien'}
Crear una copia de un diccionario

[19]
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }

copy_dictionary = pol_esp_dictionary.copy()
print(copy_dictionary)
Las tuplas y los diccionarios pueden trabajar juntos
Se ha preparado un ejemplo sencillo, mostrando como las tuplas y los diccionarios pueden trabajar juntos.

Imaginemos el siguiente problema:

necesitas un programa para calcular los promedios de tus alumnos;
el programa pide el nombre del alumno seguido de su calificación; los nombres son ingresados en cualquier orden;
el ingresar un nombre vacío finaliza el ingreso de los datos (Nota 1: ingresar una puntuación vacía generará la excepción ValueError, pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el segundo parte de la serie del curso Fundamentos de Python)
una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.
Observa el código en el editor, se muestra la solución.

[ ]

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:

Ahora se analizará línea por línea:

línea 1: crea un diccionario vacío para ingresar los datos; el nombre del alumno 
         es empleado como clave, mientras que todas las calificaciones asociadas son almacenadas 
         en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema)
línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado)
línea 4: se lee el nombre del alumno aquí;
línea 5-6: si el nombre es una cadena vacía (), salimos del bucle;
línea 8: se pide la calificación del estudiante (un valor entero en el rango del 0-10)
línea 9-10: si la puntuación ingresada no está dentro del rango de 0 a 10, se abandona el bucle;
línea 12-13: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla 
             asociada con la nueva calificación (observa el operador +=)
línea 14-15: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada 
             nueva, su valor es una tupla de un solo elemento la cual contiene la calificación ingresada;
línea 17: se itera a través de los nombres ordenados de los estudiantes;
línea 18-19: inicializa los datos necesarios para calcular el promedio (sum y counter).
línea 20-22: se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
línea 23: se calcula e imprime el promedio del alumno junto con su nombre.
'''