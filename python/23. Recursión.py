#Función recursiva para determinar cuál es la posición de un número en la posición Fibonacci (la sucesión fibonacci es 0, 1, 1, 2, 3, 5, 8, 13, 21...)
def fibonacci (n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci (8))

#Esta es una función recurvisa que nos hace un conteo regresivo desde un número dado
def conteo (x):
    if x == 0:
        return x
    else:
        print(x)
        return conteo(x-1)
        
print(conteo(15))

#Esta es una función recurvisa que nos hace un conteo ascendente desde un número dado hasta otro número dado a la función
def conteo_ascendente(initial, final):
    if initial == final:
        return initial
    else:
        print(initial)
        return conteo_ascendente(initial+1, final)
    
print(conteo_ascendente(5, 15))
            