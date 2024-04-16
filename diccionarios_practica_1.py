'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y 
el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, 
correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. 
El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, 
(5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el 
programa tendrá que hacer lo siguiente:

    Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    Preguntar por el NIF del cliente y mostrar sus datos.
    Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    Terminar el programa.
'''
from os import system
import time

def barraProgreso():
    cadena = "-" * 50
    caracter = '#'
    b = 0
    
    for i in range(100):
        if i % 2 == 0:
            x = list(cadena)
            x[b] = caracter
            cadena = "".join(x)
            b+=1
            
        print(f"[{cadena}]{i+1}%", end="\r")
        time.sleep(0.01)
    print("\n")

db_clientes = {} # Base de datos de clientes

while True:
    system("clear")
    print("-"*50)
    print("-"*16, "MENU DE OPCIONES", "-"*16)
    print("-"*50)
    print("| 1. Añadir cliente", (50 - len("| 1. Añadir cliente") - 3)*" ", "|")
    print("| 2. Eliminar cliente", (50 - len("| 2. Eliminar cliente") - 3)*" ", "|")
    print("| 3. Mostrar cliente", (50 - len("| 3. Mostrar cliente") - 3)*" ", "|")
    print("| 4. Listar todos los clientes", (50 - len("| 4. Listar todos los clientes") - 3)*" ", "|")
    print("| 5. Listar clientes preferentes", (50 - len("| 5. Listar clientes preferentes") - 3)*" ", "|")
    print("| 6. Salir", (50 - len("| 6. Salir") - 3)*" ", "|")
    print("-"*50)
    op = int(input("-> "))
    
    if op == 1:
        system("clear")
        print("-"*50)
        print("-"*17, "AÑADIR CLIENTE", "-"*17)
        print("Ingrese los datos del cliente:")
        print("-"*50)
        print("NIF:")
        nif = input("-> ")
        print("Nombre:")
        nombre = input("-> ")
        print("Dirección:")
        direccion = input("-> ")
        print("Teléfono:")
        telefono = input("-> ")
        print("Correo:")
        correo = input("-> ")
        print("¿Es cliente preferente? (S/N):")
        preferente = (input("-> ")).upper()
        
        if preferente == "S":
            preferente = True
        else:
            preferente = False
            
        db_clientes[nif] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": preferente
        }
        barraProgreso()
        input("Cliente guardado exitosamente.\n[Presione Enter para continuar...]")
    elif op == 2:
        system("clear")
        print("-"*50)
        print("-"*16, "ELIMINAR CLIENTE", "-"*16)
        print("Ingrese el NIF del cliente a eliminar:")
        print("-"*50)
        nif = input("-> ")
        if nif in db_clientes:
            del db_clientes[nif]
            print("Cliente eliminado correctamente.")
        else:
            print("El cliente no existe.")
        input("[Presione Enter para continuar...]")
    elif op == 3:
        system("clear")
        print("-"*50)
        print("-"*17, "MOSTRAR CLIENTE", "-"*16)
        print("Ingrese el NIF del cliente a mostrar:")
        print("-"*50)
        nif = input("-> ")
        if nif in db_clientes:
            print("| NIF:", nif)
            print("| Nombre:", db_clientes[nif]["nombre"])
            print("| Dirección:", db_clientes[nif]["direccion"])
            print("| Teléfono:", db_clientes[nif]["telefono"])
            print("| Correo:", db_clientes[nif]["correo"])
            print("| Preferente:", db_clientes[nif]["preferente"])
            print("-"*50)
        else:
            print("El cliente no existe.")
        input("[Presione Enter para continuar...]")
    elif op == 4:
        system("clear")
        print("-"*50)
        print("-"*12, "LISTAR TODOS LOS CLIENTES", "-"*11)
        print("-"*50)
        print("\n\n")
        iterador = 1
        for nif, cliente in db_clientes.items():
            print("*"*50)
            print("*"*20,"Cliente", iterador, "*"*19)
            print("*"*50)
            print("| NIF:", nif)
            print("| Nombre:", cliente["nombre"])
            print("| Dirección:", cliente["direccion"])
            print("| Teléfono:", cliente["telefono"])
            print("| Correo:", cliente["correo"])
            print("| Preferente:", cliente["preferente"])
            print("*"*50, end="\n\n")
            iterador += 1
        input("[Presione Enter para continuar...]")
    elif op == 5:
        system("clear")
        print("-"*50)
        print("-"*12, "LISTAR CLIENTES PREFERENTES", "-"*11)
        print("-"*50)
        iterador = 1
        for nif, cliente in db_clientes.items():
            if cliente["preferente"]:
                print("*"*50)
                print("*"*20,"Cliente", iterador, "*"*19)
                print("*"*50)
                print("| NIF:", nif)
                print("| Nombre:", cliente["nombre"])
                print("| Dirección:", cliente["direccion"])
                print("| Teléfono:", cliente["telefono"])
                print("| Correo:", cliente["correo"])
                print("| Preferente:", cliente["preferente"])
                print("*"*50, end="\n\n")
        input("[Presione Enter para continuar...]")
    elif op == 6:
        break
    else:
        print("Opción no válida.")
        input("[Presione Enter para continuar...]")
        