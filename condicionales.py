"""
ESTRUCTURAS CONDICIONALES IF: Para poder escribir programas utiles, casi siempre vamos a necesitar la 
capacidad de comprobar condiciones y cambiar el comportamiento del programa de acuerdo a ellas.
Las sentencias condicionales nos proporcionan esa capacidad.
"""

#CONDICIONALES ANIDADOS
if True:
    print("Mensaje dentro del condicional 1")
    if True:
        print("Mensaje dentro del condicional 2")
    print("Fuera del condicional 2")
print("Mensaje fuera del ambos condicionales")

#CONDICIONAL IF ELSE Y ELIF
if False:
    print("Condicion if")
else:
    print("COndicion else")
    
if False:
    print("Condicion if")
elif False:
    print("Primer elif")
elif False:
    print("Segundo elif")
else:
    print("Ninguna condicion se cumplio")


x = 5
if x > 0:
    print("x es positivo")

if x % 2 == 0:
    print("x es par")
else:
    print("x es impar")
    
"""
Algunas veces hay más de dos posibilidades, de modo que necesitamos más de dos ramas. 
Una forma de expresar una operacion como esa es usar un condicional encadenado:
"""
x = 7
y = 9
if x < y:
  print("X es menor que y")
elif x > y:
  print("X es mayor que y")
else:
  print("X e Y son iguales")