'''
Recursividad
Este termino puede describir muchos conceptos distintos, pero uno de 
ellos, hace referencia a la programación computacional.
Aquí, la recursividad es una técnica donde una función se invoca a si misma.

Tanto el factorial como la serie Fibonacci, son las mejores opciones para ilustrar este fenómeno.

¿Estás familiarizado con la serie Fibonacci?

Son una secuencia de números enteros los cuales siguen una regla sencilla:

el primer elemento de la secuencia es igual a uno (Fib1 = 1)
el segundo elemento también es igual a uno (Fib2 = 1)
cada número después de ellos son la suman de los dos números anteriores (Fibi = Fibi-1 + Fibi-2)
Aquí están algunos de los primeros números en la serie Fibonacci:

fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13

La serie de Fibonacci es un claro ejemplo de recursividad. Ya te dijimos que:
Fibi = Fibi-1 + Fibi-2
El número i se refiere al número i-1, y así sucesivamente hasta llegar a los primeros dos.
¿Puede ser empleado en el código? Por supuesto que puede. Puede hacer el código más corto y claro.
'''

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(1, 10):
    print(fib(i))

'''
El factorial también tiene un lado recursivo. Observa:
n! = 1 × 2 × 3 × ... × n-1 × n

Es obvio que:
1 × 2 × 3 × ... × n-1 = (n-1)!

Entonces, finalmente, el resultado es:
n! = (n-1)! × n

Esto se empleará en nuestra solución.
'''

def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial(n - 1)

print("Ingrese el numero del cual desea saber su factorial")
num = int(input(": "))
print("El factorial de [", num, "] es: ", factorial(num))