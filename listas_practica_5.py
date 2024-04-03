'''
Imagina una lista - no muy larga ni muy complicada, solo una lista simple que 
contiene algunos números enteros. Algunos de estos números pueden estar repetidos, y 
esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.

Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista.
El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.

Nota: Asume que la lista original está ya dentro del código - no tienes que ingresarla 
desde el teclado. Por supuesto, puedes mejorar el código y agregar una parte que pueda 
llevar a cabo una conversación con el usuario y obtener todos los datos.

Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal - no 
necesitas actualizar la lista actual.
'''

numeros = []

while True:
    print("Bienvenido al sistema de eliminacion de repeticiones")
    print("1. Ingresar numero")
    print("2. Mostrar lista")
    print("3. Eliminar repeticiones")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        numero = int(input("Ingrese un numero: "))
        numeros.append(numero)
    elif opcion == 2:
        print(numeros)
    elif opcion == 3:
        #FORMA 1
        numeros = list(set(numeros))
        print("Lista sin repeticiones: ",numeros)
        '''
        #FORMA 2
        nueva_lista = []
        for numero in numeros:
            if numero not in nueva_lista:
                nueva_lista.append(numero)
        print("Lista sin repeticiones: ",nueva_lista)
        '''
    elif opcion == 4:
        break
    else:
        print("Opcion invalida")