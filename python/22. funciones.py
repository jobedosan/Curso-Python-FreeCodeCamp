#Definición de función sin parámetro
def mostrar_mensaje():
    print("hola")
#Llamada de una función sin argumentos (se llama varias veces)
mostrar_mensaje()
mostrar_mensaje()
mostrar_mensaje()
mostrar_mensaje()

#Definicion de función con parámetros
def sumar (x, y):
    print(x + y)
    
sumar(75, 25)

#Llamada a variable que contiene el valor de retorno de la función
def multiplicar (x, y):
    return x * y

resultado_1 = multiplicar(5, 5)

print(resultado_1)
    
#Llamada a variable que contiene el resultado de una función. La función no tiene return, así que se mostrará el valor none al tratar de imprimirla en la pantalla, para que nos muestre el resultado de una función utilizado como valor de una variable deberemos utilizar siempre la palabra return.
def multiplicar (x, y):
    print(x * y)

resultado_2 = multiplicar(10, 10)

print(resultado_2)

#Definición de función con variable global (z)
x = 6

def duplicar (z):
    print(z * 2)
    
duplicar(6)

#Intento de imprimir la variable z, no funcionará porque solo existe dentro de la función duplicar, es una variable de alcance local por eso no funciona cuando tratamos de imprimirla (la siguiente línea estará comentada porque el programa se detiene al detectar que la variable no existe en el programa principal).

#print(z)

#Utilizar el valor de retorno de una función en una operación, esto es lo que nos permite el return

print(resultado_1 + resultado_1)
