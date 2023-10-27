#En el siguiente código se comentará cada línea que provoque un error, la idea es ver cómo aparece cada error por consola cuando ocurre en un programa. Para poder ver cada error será necesario descomentar el código correspondiente

#IndexError, se muestra porque el caracter al que intentamos acceder en la cadena de texto no existe

#print("Hola, cocacola"[89])

#KeyError, se muestra cuando intentamos acceder a una clave que no existe en un diccionario

'''points = {"Jose" : 20, "Aniuska" : 34, "Andrea" : 82}
print(points["Pedro"])'''

#NameError, aparece cuando el programa no reconoce una variable porque esta no ha sido definida

#print(perro_con_hambre)

#ZeroDivisionError, ocurre cuando se trata de dividir un número entre cero

#print(5 / 0)

#RecursionError, ocurre cuando hay u error en una función recursiva, es decir, cuando el parámetro que se usará en la parte recursiva del código no varía, por lo que nunca se llega al caso base que detendrá a la función

'''def conteo(num):
    if num == 0:
        print(f"Llegamos a {num}")
    else:
        print(num)
        conteo(num)

conteo(10)'''

#