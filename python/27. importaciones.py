#Importaremos el módulo math de la forma más recomendable en la siguiente línea
import math
#Con la siguiente línea imprimimos el valor de la constante pi
print(math.pi)

#Con la siguiente línea llamamos la función pow perteneciente al módulo math
print(math.pow(9, 2))


#Con la siguiente línea llamamos de forma poco usual a la función randint del módulo random para generar un número al azar desde un rango seleccionado
from random import randint
print(randint(1,20))

#Con la siguiente línea importamos de forma poco usual a la constante tau, aplicamos un nombre alternativo a la constante, la constante se llama mate ahora
from math import tau as mate
print(mate)

#Ahora importamos de forma recomendable pero cambiamos el nombre del módulo
import math as mates
print(mates.pi)