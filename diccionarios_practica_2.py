'''
Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por 
una divisa y muestre su símbolo o un mensaje de aviso si la divisa n
o está en el diccionario.
'''

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

moneda = input("Ingrese una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está en el diccionario"))