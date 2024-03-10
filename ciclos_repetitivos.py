"""
Los PCs se suelen utilizar a menudo para automatizar tareas repetitivas. Repetir tareas identicas 
o muy similares sin cometer errores es algo que a las maquinas se les da bien y en cambio a 
las personas no. Como las iteraciones resultan tan habituales, Python proporciona varias características 
en su lenguaje para hacerlas más sencillas. Una forma de iteración en Python es la sentencia while. 
He aquí un programa sencillo que cuenta hacia atrás desde cinco y luego dice “¡Despegue!”.
"""
n = 5
while n > 0:
  print(n)
  n = n - 1#Forma alternativa de hacerlo: n -= 1
print('DESPEGUE!!')

"""
Casi se puede leer la sentencia while como si estuviera escrita en inglés. Signiﬁca, “Mientras n sea mayor 
que 0, muestra el valor de n y luego reduce el valor de n en 1 unidad. Cuando llegues a 0, sal de la sentencia 
while y muestra la palabra ¡Despegue!”

El cuerpo del bucle debe cambiar el valor de una o más variables, de modo que la condición pueda en 
algún momento evaluarse como falsa y el bucle termine. La variable que cambia cada vez que el bucle se 
ejecuta y controla cuándo termina éste, recibe el nombre de variable de iteración. Si no hay variable de 
iteración, el bucle se repetirá para siempre, resultando así un bucle inﬁnito.

La sentencia break en python permite finalizar un blucle directamente, sin esperar que la condicion se cumpla
"""

while True:
  linea = input(">")
  if linea =="fin":
    break
  print(linea)
print("Terminado")

"""
SENTENCIA CONTINUE: Algunas veces, estando dentro de un bucle se necesita terminar con la iteración actual y 
saltar a la siguiente de forma inmediata. En ese caso se puede utilizar la sentencia continue para pasar a la 
siguiente iteración sin terminar la ejecución del cuerpo del bucle para la actual. A continuación se muestra un 
ejemplo de un bucle que repite lo que recibe como entrada hasta que el usuario escribe “ﬁn”, pero trata 
las líneas que empiezan por el carácter almohadilla como líneas que no deben mostrarse en pantalla (algo parecido a 
lo que hace Python con los comentarios).
"""

while True:
  linea = input("> ")
  if linea[0] == '#':
    continue
  if linea == 'fin':
    break
  print(linea)
print('Terminado!!')

'''
BUCLES DEFINIDOS USANDO FOR: A veces se desea repetir un bucle a través de un conjunto de cosas, como una lista 
de palabras, las líneas de un archivo, o una lista de números. tiene una lista de cosas para recorrer, se puede 
construir un bucle deﬁnido usando una sentencia for. A la sentencia while se la llama un bucle indeﬁnido, porque 
simplemente se repite hasta que cierta condición se hace Falsa, mientras que el bucle for se repite a través de 
un conjunto conocido de elementos, de modo que ejecuta tantas iteraciones como elementos hay en el conjunto.
'''

for item in range(1,10):
  print(item)