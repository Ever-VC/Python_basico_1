'''
El diccionario es otro tipo de estructura de datos de Python. No es 
una secuencia (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable.
'''

# Crear un diccionario con sangría francesa
diccionario = {
    "nombre": "Carlos",
    "edad": 22,
    "cursos": ["Python","Django","JavaScript"]
}
print(diccionario)

# Acceder a los elementos de un diccionario
print(diccionario["nombre"])# SALIDA ESPERADA: Carlos
print(diccionario.get("edad"))# SALIDA ESPERADA: 22

# Modificar un diccionario
diccionario["nombre"] = "Juan"
print(diccionario)# SALIDA ESPERADA: {'nombre': 'Juan', 'edad': 22, 'cursos': ['Python', 'Django', 'JavaScript']}

# Iterar un diccionario
for key in diccionario:
    print(key, ":", diccionario[key])

# Iterar un diccionario con items()
for key, value in diccionario.items():
    print(key, ":", value)

# Iterar solo las claves de un diccionario
for key in diccionario.keys():
    print(key)

# Iterar solo los valores de un diccionario
for value in diccionario.values():
    print(value)

# Ordenar un diccionario
diccionario_ordenado = dict(sorted(diccionario.items()))
print(diccionario_ordenado)

# Verificar si una clave existe en un diccionario
print("nombre" in diccionario)# SALIDA ESPERADA: True
print("telefono" not in diccionario)# SALIDA ESPERADA: True

# Agregar un elemento a un diccionario
diccionario["telefono"] = "123456789"
print(diccionario)# SALIDA ESPERADA: {'nombre': 'Juan', 'edad': 22, 'cursos': ['Python', 'Django', 'JavaScript'], 'telefono': '123456789'}

# Agregar varios elementos a un diccionario
diccionario.update({"ciudad": "Lima", "pais": "Peru"})

# Eliminar un elemento de un diccionario
del diccionario["telefono"]
print(diccionario)# SALIDA ESPERADA: {'nombre': 'Juan', 'edad': 22, 'cursos': ['Python', 'Django', 'JavaScript'], 'ciudad': 'Lima', 'pais': 'Peru'}

# Eliminar un elemento de un diccionario con pop()
diccionario.pop("nombre")
print(diccionario)# SALIDA ESPERADA: {'edad': 22, 'cursos': ['Python', 'Django', 'JavaScript'], 'ciudad': 'Lima', 'pais': 'Peru'}

# Eliminar el último elemento de un diccionario
diccionario.popitem()
print(diccionario)# SALIDA ESPERADA: {'nombre': 'Juan', 'edad': 22, 'cursos': ['Python', 'Django', 'JavaScript'], 'ciudad': 'Lima'}

# Eliminar todos los elementos de un diccionario
diccionario.clear()

# Eliminar un diccionario
del diccionario

# Crear un diccionario con dict()
diccionario = dict(nombre="Carlos", edad=22, cursos=["Python","Django","JavaScript"])
print(diccionario)# SALIDA ESPERADA: {'nombre': 'Carlos', 'edad': 22, 'cursos': ['Python', 'Django', 'JavaScript']}

# Copiar un diccionario
diccionario_copia = diccionario.copy()

# Crear un diccionario con claves de otro diccionario
diccionario = dict.fromkeys(diccionario)
print(diccionario)# SALIDA ESPERADA: {'nombre': None, 'edad': None, 'cursos': None}

# Obtener las claves de un diccionario
print(diccionario_copia.keys())# SALIDA ESPERADA: dict_keys(['nombre', 'edad', 'cursos'])