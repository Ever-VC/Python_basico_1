'''
Escribe un programa en Python que tome un párrafo y permita contar cuantas veces aparece una
palabra en dicho párrafo. La frase y la palabra deben ser ingresadas por el usuario.
'''

parrafo = input("Ingrese un parrafo: ")
palabra = input("Ingrese una palabra a buscar: ")

print("La palabra",palabra,"aparece",parrafo.lower().count(palabra.lower()),"veces" if parrafo.lower().count(palabra.lower()) > 1 else "vez")# SALIDA ESPERADA: La palabra hola aparece 2 veces