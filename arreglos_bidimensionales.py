'''
A menudo encontramos estos arreglos en nuestras vidas. Probablemente el mejor 
ejemplo de esto sea un tablero de ajedrez.

Un tablero de ajedrez está compuesto de filas y columnas. Hay ocho filas 
y ocho columnas. Cada columna está marcada con las letras de la A a la H. 
Cada línea está marcada con un número del uno al ocho.

La ubicación de cada campo se identifica por pares de letras y dígitos. 
Por lo tanto, sabemos que la esquina inferior derecha del tablero 
(la que tiene la torre blanca) es A1, mientras que la esquina opuesta es H8.

Supongamos que podemos usar los números seleccionados para representar 
cualquier pieza de ajedrez. También podemos asumir que cada fila en el tablero 
de ajedrez es una lista.

Supongamos también que un símbolo predefinido denominado '0' designa 
un campo vacío en el tablero de ajedrez.

Entonces, si queremos crear una lista de listas que representan todo el 
tablero de ajedrez, se puede hacer de la siguiente manera:
'''

tablero = []

for i in range(8):
    fila = [0 for j in range(8)]
    tablero.append(fila)

for fila in tablero:
    print(fila)

'''
Nota:

*   la parte interior del bucle crea una fila que consta de ocho elementos 
    (cada uno de ellos es igual a 0) y lo agrega a la lista del tablero;
*   la parte exterior se repite ocho veces;
    en total, la lista tablero consta de 64 elementos (todos iguales a 0).

Este modelo imita perfectamente el tablero de ajedrez real, que en realidad 
es una lista de elementos de ocho elementos, todos ellos en filas individuales. 
Resumamos nuestras observaciones:

*   los elementos de las filas son campos, ocho de ellos por fila;
*   los elementos del tablero de ajedrez son filas, ocho de ellos por tablero de ajedrez.

La variable tablero ahora es un arreglo bidimensional. También se le llama, por 
analogía a los términos algebraicos, una matriz.

Como las listas de comprensión puede ser anidadas, podemos acortar la creación del tablero de la siguiente manera:
'''

tablero = [[0 for j in range(8)] for i in range(8)] # La parte interna crea una fila, y la parte externa crea una lista de filas.
print("-"*30)
for fila in tablero:
    print(fila)