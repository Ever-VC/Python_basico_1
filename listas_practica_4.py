'''
Desarrolla un programa en Python que analice datos meteorológicos históricos. El programa debe
tomar como entrada datos de temperatura diaria durante un período de tiempo y calcular
estadísticas como la temperatura media, la temperatura más alta, la temperatura más baja y los
días de helada (cuando la temperatura cae por debajo de cero).
'''

temperaturas = []

while True:
    print("Bienvenido al sistema de analisis de datos meteorologicos")
    print("1. Ingresar temperatura")
    print("2. Mostrar estadisticas")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        temperatura = float(input("Ingrese la temperatura: "))
        temperaturas.append(temperatura)
    elif opcion == 2:
        if len(temperaturas) == 0:
            print("[NO HAY TEMPERATURAS]")
        else:
            print("Temperatura media: ",sum(temperaturas)/len(temperaturas))
            print("Temperatura mas alta: ",max(temperaturas))
            print("Temperatura mas baja: ",min(temperaturas))
            heladas = 0
            for temperatura in temperaturas:
                if temperatura <= 0:
                    heladas += 1
            print("Dias de helada: ",heladas)
    elif opcion == 3:
        break
    else:
        print("Opcion invalida")