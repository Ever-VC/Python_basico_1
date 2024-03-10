"""
Los operadores aritméticos son simbolos especiales que representan calculos, como la suma o la multiplicacion. 
Los valores a los cuales se aplican esos operadores reciben el nombre de operandos.
"""

#SUMA
resultado_suma = 1 + 2
print(resultado_suma)# SALIDA ESPERADA: 3

#OPERACIONES CON EXPRESIONES
"""
Una expresion es una combinacion de valores, variables y opreciones. Un valor por si mismo se considera una 
expresion, y tambien lo es una variable asi que las siguientes expresiones son todas validas.
"""

x = 5
x = x + 7
print(x) # SALIDA ESPERADA: 12

"""
Cuando en una expresion aparece más de un operador, el orden de la evaluacion depende de las reglas de precedencia.
Para los operadores matemáticos, python sigue las convenciones matemáticas. el acronimo PEDMSR resulta util para 
recordar esas reglas.

    -> Primero se ejecuta lo que se encuentre entre parentesis.
    -> Segundo se evalua los terminos con exponentes.
    -> Tercero se evalua la multiplicacion.
    -> cuarto se evalua la division.
    -> Quinto se evalua la suma.
    -> Sexto se evalua la resta.
"""

print(2*(3-1))# SALIDA ESPERADA: 4
print((1+1)**(5-2))# SALIDA ESPERADA: 8
numero_minutos = int(input("Ingrese el numero de minutos -> "))# 60 minutos = 1 hora
print((numero_minutos*100)/60)# SALIDA ESPERADA: 100