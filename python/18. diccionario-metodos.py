#Estructura de diccionario
diccionario = {"a": 1, "b": 2,"c": 3,"d": 4,"e": 5}

#Acceso a valor contenido en un diccionario
print(diccionario["a"])
print(diccionario.get("a"))

#Añadir par clave-valor al diccionario
diccionario["f"] = "6"
print(diccionario)

#Modificar par clave-valor del diccionario
diccionario["f"] = "4"
print(diccionario)

#Remover par clave-valor del diccionario
del diccionario["f"]
print(diccionario)

#Revisar existencia de un elemento del diccionario
print("b" in diccionario)
print("f" in diccionario)