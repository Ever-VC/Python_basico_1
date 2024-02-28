# ----------------- SECUENCIAS DE ESCAPE -----------------

# \n: Salto de línea
msg = 'Primera linea \nSegunda linea \nTercera linea'
print(msg)

# \t: Tabulación
msg = '| Nombre\t| Edad \t| Sexo |'
valores = '| Ever Samuel \t| 25 \t| M    |'
print(msg)
print(valores)

# \b: Retroceso
msg = '123456\b7890'
print(msg)
msg = '123456\b\b7890'
print(msg)
msg = '123456\b\b\b7890'
print(msg)

# \' : Comilla simple
msg = 'El alumno dijo: \'Presente\''
print(msg)

# \" : Comilla doble
msg = "El alumno dijo: \"Presente\""
print(msg)

# \\ : Diagonal invertida 
msg = "C:\\Users\\admin\\Documents"
print(msg)

# ----------------- EXPRESIONES LITERALES -----------------
# r: Indica que la cadena es cruda (raw data)
text = 'abc\ndef' # SALIDA ESPERADA: 'abc\ndef'
print(text)

text = r'abc\ndef' # SALIDA ESPERADA: 'abc\ndef'
print(text)

text = 'a\tb\tc'
print(text)

text = r'a\tb\tc'
print(text)

# ----------------- OPERACIONES CON PRINT -----------------

msg1 = 'Sabes por que estoy aca?'
msg2 = 'Porque me gusta programar'
print(msg1, msg2) # Por defecto el separador es un espacio

print(msg1, msg2, sep='|') # Cambiando el separador por un '|'

print(msg2, end='!!\n') # Cambiando el separador por un '|' y el final por '!'

# ----------------- OPERACIONES CON PRINT -----------------


#Combinar dos o más cadenas de texto utilizando el operador +
msg1 = 'Hola'
msg2 = 'Mundo'
print(msg1 + ' ' + msg2)

#Repetir una cadena de texto utilizando el operador *
msg = 'Hola'
print(msg * 3)

msg = "Esta es una cadena de texto"
print(msg[6]) # SALIDA ESPERADA: s

print(msg[5:10]) # SALIDA ESPERADA: es un

print(msg[:4]) # SALIDA ESPERADA: Esta

print(msg[5:]) # SALIDA ESPERADA: es una cadena de texto

print(msg[-1]) # SALIDA ESPERADA: o

print(msg[-4:]) # SALIDA ESPERADA: texto

print(msg[::2]) # SALIDA ESPERADA: Esae n aad eto

print(msg[::-1]) # SALIDA ESPERADA: otxet ed anedac anu se atsE

# ----------------- FUNCIONES DE CADENAS -----------------

# len(): Retorna el tamaño de la cadena
msg = "Hola mundo"
print( len(msg)) # SALIDA ESPERADA: 10

# upper(): Convierte una cadena a mayúsculas
msg = 'hola mundo'
print(msg.upper()) # SALIDA ESPERADA: HOLA MUNDO

# lower(): Convierte una cadena a minúsculas
msg = 'HOLA MUNDO'
print(msg.lower()) # SALIDA ESPERADA: hola mundo

# in: Verifica si una palabra o letra existe en una cadena
msg = "Hola mundo"
print("u" in msg) # SALIDA ESPERADA: True

# strip(): Crea una nueva cadena eliminando los espacios que hay en la cadena original
print( msg.strip()) # SALIDA ESPERADA: Hola mundo

# lstrip(): Crea una nueva cadena eliminando los espacios del INICIO que hay en la cadena original
# rstrip(): Crea una nueva cadena eliminando los espacios del FINAL que hay en la cadena original

# startswith(): Retorna True o False si la palabra existe al inicio de la cadena
msg = "Hola Mundo"
print(msg.startswith("Mundo")) # SALIDA ESPERADA: False

# startswith(): Retorna True o False si la palabra existe al final de la cadena
print(msg.endswith("Mundo")) # SALIDA ESPERADA: True

#fin(): Retorna la posición de la primera ocurrencia de la palabra o letra buscada en una cadena
print(msg.find("Mundo")) # SALIDA ESPERADA: 5

# count(): Retorna la cantidad de ocurrencias de la palabra o letra buscada en una cadena
print(msg.count("2")) # SALIDA ESPERADA: 0

# replace(): Cambia el valor específico de una cadena por otro indicado como parámetro
#Si hay mayor ocurrencias del primer parámetro, se pone como tercer parámetro la cantidad de veces que se desea reemplezar
print( msg.replace("mundo", "clase")) # SALIDA ESPERADA: Hola clase

# idigit(): Verifica si el contenido de la cadena es un número
msg = "3"
print( msg.isdigit()) # SALIDA ESPERADA: True

# isalpha(): Verifica si el contenido de la cadena son letras (sin espacios o caracteres especiales)
msg = "mensaje"
print( msg.isalpha()) # SALIDA ESPERADA: True

# isalnum(): Verifica si el contenido de la cadena son letras o números (sin espacios o caracteres especiales)
msg = "HolaMundo2"
print( msg.isalnum()) # SALIDA ESPERADA: True
