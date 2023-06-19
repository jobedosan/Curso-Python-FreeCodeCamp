#Ciclo for iterando una cadena de caracteres
letras = "a", "b", "c", "d"
for char in letras:
    print(char)

#Ciclo for iterando una lista
letras = ["a", "b", "c", "d"]
for char in letras:
    print(char)

#Ciclo for iterando una tupla
letras = ("a", "b", "c", "d")
for char in letras:
    print(char)

#Ciclo for iterando las claves de un diccionario
letras = {"a":1, "b":2, "c":3, "d":4}
for clave in letras:
    print(clave)

#Ciclo for iterando los valores de un diccionario
letras = {"a":1, "b":2, "c":3, "d":4}
for valor in letras.values():
    print(valor)
    
#Ciclo for iterando los pares clave valor de un diccionario
letras = {"a":1, "b":2, "c":3, "d":4}
for clave, valor in letras.items():
    print(clave, valor)
    
