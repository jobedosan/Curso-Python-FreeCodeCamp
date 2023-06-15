#Función input
valor_1 = input(" ingresa un número: ") 
print(valor_1)
valor_2 = input(" ingresa True o False: ")
print(valor_2)
valor_3 = input(" ingresa un texto: ")
print(valor_3)

#La función input siempre retornará un string
print(type(valor_1))
print(type(valor_2))
print(type(valor_2))

#En el caso de necesitar un tipo de dato distinto debemos encerrar el input en una función que transforme el dato ingresado por el usuario en otro tipo de dato

#La función int se utiliza para convertir la cadena de texto en un dato numérico entero
valor_4 = int(input("Ingresa un número: "))
print(valor_4)
print(type(valor_4))