#Condicional if (si se cumple imprime el resultado por consola, en caso contrario no)
#La siguiente condicional se cumple
temp = 15
if temp <25:
    print("Muy frío")

#La siguiente condicional no se cumple, no muestra nada por consola
temp = 30
if temp <25:
    print("Muy frío")

#Condicional if con cláusula 'else'
#La siguiente condicional ejecuta el código del if
temp = 15
if temp < 25:
    print("Muy frío")
else:
    print("Calor")
#La siguiente condicional ejecuta el código del else
temp = 26
if temp < 25:
    print("Muy frío")
else:
    print("Calor")

#Condicional if con cláusula 'else' y cláusula 'elif' (se ejecuta el código del if)
temp = 0
if temp <= 0:
    print("Muy frío")
elif temp < 25:
    print("Frío")
else:
    print("Calor")
    
#Condicional if con cláusula 'else' y cláusula 'elif' (se ejecuta el código del elif)
temp = 15
if temp <= 0:
    print("Muy frío")
elif temp < 25:
    print("Frío")
else:
    print("Calor")
    
#Condicional if con cláusula 'else' y cláusula 'elif' (se ejecuta el código del else)
temp = 36
if temp <= 0:
    print("Muy frío")
elif temp < 25:
    print("Frío")
else:
    print("Calor")
    