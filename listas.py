numeros = [1,2,3,4,5,6,7,8,9,10,10]
print(numeros)# SALIDA ESPERADA: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
print(numeros[::-1])# SALIDA ESPERADA: [10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#Muestra True si 5 esta en la lista de numeros
print(5 in numeros)# SALIDA ESPERADA: True

materias = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
print(sorted(materias))# SALIDA ESPERADA: ['Fisica', 'Historia', 'Lengua', 'Matematicas', 'Quimica']

materias.insert(3, "Programacion")
print(materias)# SALIDA ESPERADA: ['Matematicas', 'Fisica', 'Quimica', 'Programacion', 'Historia', 'Lengua']

materias.append("Ingles")
print(materias)# SALIDA ESPERADA: ['Matematicas', 'Fisica', 'Quimica', 'Programacion', 'Historia', 'Lengua', 'Ingles']

materias.remove("Historia")
print(materias)# SALIDA ESPERADA: ['Matematicas', 'Fisica', 'Quimica', 'Programacion', 'Lengua', 'Ingles']

materias.pop(3)
print(materias)# SALIDA ESPERADA: ['Matematicas', 'Fisica', 'Quimica', 'Lengua', 'Ingles']

del materias[3]
print(materias)# SALIDA ESPERADA: ['Matematicas', 'Fisica', 'Quimica', 'Ingles']

numeros[8] = 11
print(numeros)# SALIDA ESPERADA: [1, 2, 3, 4, 5, 6, 7, 8, 11, 10, 10]
print("El numero mayor de la lista es",max(numeros))# SALIDA ESPERADA: El numero mayor de la lista es 11
print("El numero menor de la lista es",min(numeros))# SALIDA ESPERADA: El numero menor de la lista es 1

numero_buscar = int(input("Ingrese un numero a buscar: "))

if numero_buscar in numeros:
    print("El numero",numero_buscar,"se encuentra en la lista y su indice es",numeros.index(numero_buscar))# SALIDA ESPERADA: El numero 5 se encuentra en la lista y su indice es 4
    print("El numero aparece", numeros.count(numero_buscar),"veces" if numeros.count(numero_buscar) > 1 else "vez")# SALIDA ESPERADA: El numero aparece 1 veces
else:
    print("El numero",numero_buscar,"no se encuentra en la lista")

print("-".join(materias))# SALIDA ESPERADA: Matematicas-Fisica-Quimica-Ingles

materias.clear()
print(materias)# SALIDA ESPERADA: []