#Estructura de tuplas
nums = (1, 2, 3)
textos = ("perro", "sol", "aro")
nums_decimal = (1.5, 2.64, 3.7)

#Accediendo a elementos de las listas, accederemos al segundo elemento de cada lista
print(nums[1])
print(textos[1])
print(nums_decimal[1])

#Agregar un elemento como último valor de cada tupla por medio del método append no es posible, ya que no son mutables, retornará un error (descomentar para ver el error)
#nums.append(4) 
#textos.append("gato")
#nums_decimal.append(6.65)

#print(nums)
#print(textos)
#print(nums_decimal)

#Agregar un elemento en un índice específico no es posible con las tuplas, ya que no son mutables, retornará un error (descomentar para ver el error)
#nums.insert(3, 5) 
#textos.insert(3, "león")
#nums_decimal.insert(3, 9.32)

#print(nums)
#print(textos)
#print(nums_decimal)

#Remover un elemento en un índice específico no es posible con las tuplas, ya que no son mutables, retornará un error (descomentar para ver el error)
#nums.remove(5) 
#textos.remove("león")
#nums_decimal.remove(9.32)

#print(nums)
#print(textos)
#print(nums_decimal)

#Método index utilizado en las tuplas, nos indicará el posicionamiento de un elemento en el índice de la lista
textos = ("perro", "sol", "aro")
#Nos retorna el índice 2 porque allí está ubicada la palabra aro
print(textos.index("sol"))

#Si tratamos de encontrar un valor inexistente en la lista con index() nos retornará un error (descomentar para ver el error)
#print(textos.index("león"))

#Cambiar elementos de una tupla por otro no es posible con las tuplas, ya que no son mutables, retornará un error (descomentar para ver el error)
#textos = ("perro", "sol", "aro")
#textos [1] = "león"
#print(textos)

#Método count nos dice cuántas ocurrencias tiene un elemento en la tupla (cuántas veces aparece)
tupla =("perro", "gato", "león", "dragón", "gato", "pato", "gato")
print(tupla.count("gato"))