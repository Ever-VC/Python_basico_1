'''
Los datos inmutables no pueden ser modificados de esta manera.
Imagina que una lista solo puede ser asignada y leída. No podrías 
adjuntar ni remover un elemento de la lista. Si se agrega un 
elemento al final de la lista provocaría que la lista se cree desde cero.

Se tendría que crear una lista completamente nueva, la 
cual contenga los elementos ya existentes más el nuevo elemento.

El tipo de datos que se desea tratar ahora se llama tupla. 
Una tupla es una secuencia inmutable. Se puede comportar como
 una lista pero no puede ser modificada en el momento.
'''

#Dos formas de crear tuplas en Python
tupla_1 = (1,2,3,4,5)
tupla_2 = 6,7,8,9,10

print(tupla_1)
print(tupla_2)

# Crear una tupla con un solo elemento
tupla_3 = (1,)
print(tupla_3)

# Crear una tupla vacia
tupla_4 = ()
print(tupla_4)

# Acceder a los elementos de una tupla
print(tupla_1[0])# SALIDA ESPERADA: 1
print(tupla_1[-1])# SALIDA ESPERADA: 5
print(tupla_1[1:])# SALIDA ESPERADA: (2, 3, 4, 5)
print(tupla_1[:-2])# SALIDA ESPERADA: (1, 2, 3)

# No se puede modificar una tupla
# tupla_1[0] = 10# ERROR

# Iterar una tupla
for numero in tupla_1:
    print(numero)

# Uniendo dos tuplas
tupla_5 = tupla_1 + tupla_2
print(tupla_5)

# Repetir una tupla
tupla_6 = tupla_1 * 2
print(tupla_6)

# Operadores in y not in en tuplas
print(5 in tupla_1)# SALIDA ESPERADA: True
print(10 not in tupla_1)# SALIDA ESPERADA: True

# Cambiando valores entre tuplas
tupla_1, tupla_2 = tupla_2, tupla_1
print(tupla_1)
print(tupla_2)

# Eliminar una tupla
del tupla_6

# Convertir una lista en una tupla
lista = [1,2,3,4,5]
tupla_7 = tuple(lista)
print(tupla_7)

# Convertir una tupla en una lista
lista_2 = list(tupla_1)
print(lista_2)