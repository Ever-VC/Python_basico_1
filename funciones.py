'''
Muy a menudo ocurre que un cierto fragmento de código se repite 
muchas veces en un programa. Se repite de manera literal o, con 
algunas modificaciones menores, empleando algunas otras variables 
dentro del programa. También ocurre que un programador ha comenzado 
a copiar y pegar ciertas partes del código en más de una ocasión 
en el mismo programa.

Puede ser muy frustrante percatarse de repente que existe un 
error en el código copiado. El programador tendrá que escarbar 
bastante para encontrar todos los lugares en el código donde 
hay que corregir el error. Además, existe un gran riesgo de 
que las correcciones produzcan errores adicionales.

Definamos la primera condición por la cual es una buena idea 
comenzar a escribir funciones propias: si un fragmento de código 
comienza a aparecer en más de una ocasión, considera la posibilidad 
de aislarlo en la forma de una función invocando la función desde 
el lugar en el que originalmente se encontraba.

Puede suceder que el algoritmo que se desea implementar sea tan 
complejo que el código comience a crecer de manera incontrolada y, 
de repente, ya no se puede navegar por él tan fácilmente.

Se puede intentar solucionar este problema comentando el código, 
pero pronto te darás cuenta que esto empeorará la situación - demasiados 
comentarios hacen que el código sea más difícil de leer y entender. 
Algunos dicen que una función bien escrita debe ser comprensible con tan solo una mirada.

Un buen desarrollador divide el código (o mejor dicho: el problema) 
en piezas aisladas, y codifica cada una de ellas en la forma de una función.

Esto simplifica considerablemente el trabajo del programa, debido a 
que cada pieza se codifica por separado, y consecuentemente se prueba 
por separado. A este proceso se le llama comúnmente descomposición.

Existe una segunda condición: si un fragmento de código se hace tan 
extenso que leerlo o entenderlo se hace complicado, considera dividirlo 
en pequeños problemas, por separado, e implementa cada uno de ellos 
como una función independiente..

Esta descomposición continúa hasta que se obtiene un conjunto de 
funciones cortas, fáciles de comprender y probar.
'''

def message():
    print("Ingresar valor: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

print("El promedio de los valores ingresados es: ", (a + b + c) / 3)

# Paso de parametros posicionales
def suma(a, b, c):
    return a + b + c
print(suma(1, 2, 3))# SALIDA ESPERADA: 6

# Paso de argumentos de palabras clave
def resta(a, b, c):
    return a - b - c
print(resta(a=1, b=2, c=3))# SALIDA ESPERADA: -4

# Mezclando argumentos posicionales y de palabras clave
def multiplicacion(a, b, c):
    return a * b * c
print(multiplicacion(1, b=2, c=3))# SALIDA ESPERADA: 6

# Paso de argumentos por defecto
def division(a, b, c=1):
    return a / b / c
print(division(1, 2))# SALIDA ESPERADA: 0.5

# Paso de un numero variable de argumentos
def promedio(*args):
    return sum(args) / len(args)
print(promedio(1, 2, 3))# SALIDA ESPERADA: 2.0

# Paso de un numero variable de argumentos de palabras clave
def promedio_ponderado(**kwargs):
    return sum(kwargs.values()) / len(kwargs)
print(promedio_ponderado(a=1, b=2, c=3))# SALIDA ESPERADA: 2.0

# Paso de argumentos por referencia
def modificar_lista(lista):
    lista.append(4)
    return lista
numeros = [1, 2, 3]
print(modificar_lista(numeros))# SALIDA ESPERADA: [1, 2, 3, 4]