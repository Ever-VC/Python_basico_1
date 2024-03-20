'''
Crea un sistema simple en Python para gestionar tareas pendientes. El programa debe permitir al
usuario agregar nuevas tareas, mostrar todas las tareas pendientes junto con su estado, y mostrar
toda la lista de tareas. (pendiente/completada).
'''

lst_tareas = []
while True:
    print("Bienvenido al sistema de gestion de tareas pendientes")
    print("1. Agregar tarea")
    print("2. Mostrar todas las tareas")
    print("2. Modificar el estado de una tarea")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        tarea = input("Ingrese la tarea a agregar: ")
        lst_tareas.append([tarea,"Pendiente"])
    elif opcion == 2:
        if len(lst_tareas) == 0:
            print("[NO HAY TAREAS]")
        else:
            iterador = 1
            print("-"*40)
            for tarea in lst_tareas:
                print("#",iterador,"|  ",tarea[0],": ",tarea[1])
                iterador += 1
            print("-"*40)
    elif opcion == 3:
        if len(lst_tareas) == 0:
            print("[NO HAY TAREAS]")
        else: 
            iterador = 1
            print("-"*40)
            for tarea in lst_tareas:
                print("#",iterador,"|  ",tarea[0],": ",tarea[1])
                iterador += 1
            print("-"*40)
            tarea_modificar = int(input("Ingrese el numero de la tarea a modificar: "))
            estado = input("Ingrese el nuevo estado de la tarea: ")
            lst_tareas[tarea_modificar-1][1] = estado.lower().title()
    elif opcion == 4:
        break
    else:
        print("Opcion invalida")
