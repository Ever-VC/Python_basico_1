#https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja#:~:text=El%20ordenamiento%20de%20burbuja%20(Bubble,est%C3%A1n%20en%20el%20orden%20equivocado.

my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)