'''
Los sets son colecciones desordenadas de elementos únicos. Se pueden pensar como diccionarios, pero solo con claves.
'''

# ---- Formas de crear sets ----

# Crear un set vacío
s = set()
print(s)# SALIDA ESPERADA: set()

# Crear un set con elementos
s = {1, 2, 3}
print(s)# SALIDA ESPERADA: {1, 2, 3}

# Crear un set con elementos repetidos
s = {1, 2, 3, 3, 3}
print(s)# SALIDA ESPERADA: {1, 2, 3}

# Crear un set a partir de una lista
s = set([1, 2, 3])

# Crear un set a partir de una cadena
s = set("Hola Mundo")
print(s)# SALIDA ESPERADA: {'H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd'}

# ---- Acceder a los elementos de un set ----

# Los sets no permiten acceder a sus elementos mediante índices, ya que son colecciones desordenadas.

# ---- Modificar un set ----

# Los sets no permiten modificar sus elementos, ya que son colecciones inmutables.

# ---- Iterar un set ----
s = {1, 2, 3}
for elemento in s:
    print(elemento)
    
# ---- Verificar si un elemento existe en un set ----
s = {1, 2, 3}
print(1 in s)# SALIDA ESPERADA: True

# ---- Agregar un elemento a un set ----
s = {1, 2, 3}
s.add(4)
print(s)# SALIDA ESPERADA: {1, 2, 3, 4}

# ---- Agregar varios elementos a un set ----
s = {1, 2, 3}
s.update([4, 5, 6])
print(s)# SALIDA ESPERADA: {1, 2, 3, 4, 5, 6}

# ---- Eliminar un elemento de un set ----
s = {1, 2, 3}
s.remove(2)
print(s)# SALIDA ESPERADA: {1, 3}

# ---- Eliminar un elemento de un set con discard() ----
s = {1, 2, 3}
s.discard(2)
print(s)# SALIDA ESPERADA: {1, 3}

# ---- Eliminar el último elemento de un set con pop() ----
s = {1, 2, 3}
s.pop()
print(s)# SALIDA ESPERADA: {2, 3}

# ---- Eliminar todos los elementos de un set ----
s = {1, 2, 3}
s.clear()
print(s)# SALIDA ESPERADA: set()

# ---- Operaciones con sets ----

# Unión de sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)# SALIDA ESPERADA: {1, 2, 3, 4, 5}

# Intersección de sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.intersection(s2)
print(s3)# SALIDA ESPERADA: {3}

# Diferencia de sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.difference(s2)
print(s3)# SALIDA ESPERADA: {1, 2}

# Diferencia simétrica de sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.symmetric_difference(s2)
print(s3)# SALIDA ESPERADA: {1, 2, 4, 5}

# Verificar si un set es subconjunto de otro set
s1 = {1, 2, 3}
s2 = {1, 2}
print(s2.issubset(s1))# SALIDA ESPERADA: True

# Verificar si un set es superconjunto de otro set
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.issuperset(s2))# SALIDA ESPERADA: True

# Verificar si dos sets son disjuntos
s1 = {1, 2, 3}
s2 = {4, 5}
print(s1.isdisjoint(s2))# SALIDA ESPERADA: True

# ---- Copiar un set ----
s = {1, 2, 3}
s_copia = s.copy()
print(s_copia)# SALIDA ESPERADA: {1, 2, 3}

# ---- Eliminar un set ----
s = {1, 2, 3}
del s