#Estructura de lista
nums = [1, 2, 3]
textos = ["perro", "sol", "aro"]
nums_decimal = [1.5, 2.64, 3.7]

#Accediendo a elementos de las listas, accederemos al segundo elemento de cada lista
print(nums[1])
print(textos[1])
print(nums_decimal[1])

#Agregaremos un elemento como último valor de cada lista por medio del método append
nums.append(4) 
textos.append("gato")
nums_decimal.append(6.65)

print(nums)
print(textos)
print(nums_decimal)

#Agregaremos un elemento como penúltimo valor por medio del método insert
nums.insert(3, 5) 
textos.insert(3, "león")
nums_decimal.insert(3, 9.32)

print(nums)
print(textos)
print(nums_decimal)

#Removeremos el último elemento agregado a cada lista
nums.remove(5) 
textos.remove("león")
nums_decimal.remove(9.32)

print(nums)
print(textos)
print(nums_decimal)

#Cuando hay varios elementos repetidos de borrará el que aparezca de primero en orden de izquierda a derecha (en este caso deja el último número 3 en la lista)
nums_repetidos = [1, 2, 3, 4, 5, 6, 7, 3]
nums_repetidos.remove(3)
print(nums_repetidos) 

#Al tratar de remover un elemento inexistente en la lista se crea un error (descomentar para ver el error)
#nums_repetidos.remove(100)

#Verificamos la existencia de un valor en la lista por medio del operador in
print(5 in nums_repetidos)
print(10 in nums_repetidos)

#Método index utilizado en las listas, nos indicará el posicionamiento de un elemento en el índice de la lista
textos = ["perro", "sol", "aro"]
#Nos retorna el índice 2 porque allí está ubicada la palabra aro
print(textos.index("aro"))

#Si tratamos de encontrar un valor inexistente en la lista con index() nos retornará un error (descomentar para ver el error)
#print(textos.index("león"))

#Cambiamos elemento de una lista por otro (cambiamos la palabra sol por león)
textos = ["perro", "sol", "aro"]
textos [1] = "león"
print(textos)
