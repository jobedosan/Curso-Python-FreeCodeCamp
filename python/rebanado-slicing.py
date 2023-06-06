#Slicing o rebanado
print("python"[1:4])
animal = "perro"
print(animal[:3])
#Slicing desde un lugar determinado hasta el final de la cadena
animal = "dinosaurio"
print(animal[2:])
#Slicing desde el inicio de la cadena hasta un final determinado
animal = "zamuro"
print(animal[:4])
#Slicing desde el inicio hasta el final de la cadena (para obtener una copia de la cadena)
animal ="rinoceronte"
print(animal [2:9])
#Slicing utilizando un caracter fuera del rango del índice de la cadena (para poder incluir el último caracter si así se desea, no importa incluso si nos excedemos por mucho, igual resultará en la inclusión del último caracter de la cadena, pero no es lo correcto)
animal ="hipopotamo"
print(animal[4:10])
print(animal[4:48])
#Parámetro paso (nos permite seleccionar la forma en que se saltará de un caracter al siguiente, la operación se hace sumando el valor del tercer parámetro al índice desde donde comienza la rebanada, en este ejemplo va del caracter 2 al 4 y del 4 al 6)
animal = "pterodáctilo"
print(animal[2:7:2])

animal = "ornitorrinco"
print(animal [2:12:4])

animal = "hipopotomonstruoesquipedaliofobia"
print(animal[3::2])

