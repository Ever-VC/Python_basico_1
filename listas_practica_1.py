'''
Escribe un programa en Python que genere un número aleatorio entre 1 y 100 y desafíe al usuario
a adivinarlo. El programa debe proporcionar pistas al usuario si el número adivinado es demasiado
alto o demasiado bajo. También debe llevar un registro del número de intentos que le tomó al
usuario adivinar el número correcto.

“La función randint(a, b) devuelve un número entero comprendido entre a y b (ambos inclusive)
de forma aleatoria.”
'''
import random

numero_aleatorio = random.randint(1,100)
contador_intentos = 0
print("Adivina el numero que estoy pensando entre 1 y 100")
while True:
    numero_usuario = int(input("Ingrese un numero: "))
    if numero_usuario == numero_aleatorio:
        print("Felicidades, adivinaste el numero en",contador_intentos,"intentos")
        break
    elif numero_usuario < numero_aleatorio:
        print("El numero es muy bajo")
    else:
        print("El numero es muy alto")
    contador_intentos += 1
    print("Intenta de nuevo")
