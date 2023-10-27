#El siguiente programa demuestra cómo funciona la estructura completa de try, except, con else y finally

num_1 = int(input("Ingresa un primer número"))
num_2 = int(input("Ingresa un segundo número"))

try:
    result = num_1 / num_2
    print(result)
except:
    result = "nulo"
    print("La operación no funcionó, este es el except")
else:
    print("La operación funcionó en el try")
finally:
    print(f"El resultado es {result}")