#Método count (cuenta la cantidad de veces que se repite un elemento)
lista_1 = [1, 2, 3, 4, 5, 3, 5, 4, 3]
print(lista_1.count(3))

#Método extend (extiende una lista integrado otra lista)
lista_2 = [1, 2, 3]
extension = [4, 5, 6, 7]
lista_2.extend(extension)
print(lista_2)

lista_3 = [1, 2, 3]
lista_3.extend([5, 6, 7, 8])
print(lista_3)

#Método .pop (elimina un elemento, lo retorna por consola)
lista_4 =[1, 2, 3, 4]
textos_2 =["silla", "balón", "papagayo"]
print(lista_4.pop())
print(textos_2.pop())
print(textos_2)
print(lista_4)

#Método .reverse (invierte el orden de los elementos en la lista)
lista_4 =[1, 2, 3, 4]
lista_4.reverse()
print(lista_4)

#Método .sort(ordena las listas en un orden específico, ascendente o descendente según orden númerico, alfabético o característica señalada por una función)
lista_5 = ["perro", "gato","león"]
lista_5.sort(reverse = False)
print(lista_5)
lista_5.sort(reverse = True)
print(lista_5)

