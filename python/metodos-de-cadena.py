#Método capitalize(), nos retorna una cadena de caracteres con inicial en mayúscula y el resto en minúscula
nombre = "benjamin"
print(nombre.capitalize())
nombre = "bENJAMIN"
print(nombre.capitalize())

#Método find(), nos retorna el índice en dónde comienza la palabra que buscamos o donde aparece por primera vez alguna letra que estemos buscando en la cadena de caracteres
frase = "Mi perro es gris con negro y amarillo"
print(frase.find("perro"))
print(frase.find("o"))
print(frase.find("rro es gris"))

#La siguiente línea busca algo que no existe en la cadena, nos retornará -1
nombre = "Benjamin"
print(nombre.find("perro"))

#Método find() con valor de inicio y final de búsqueda
palabra ="hipopotomonstruoesquipedaliofobia"
print(palabra.find("b",8,32))

#Se puede copiar solo el inicio de la búsqueda y buscará hasta el final (pero no es nada recomendable, no es buena práctica)
print(palabra.find("b",8))

#Si excedemos el valor disponible de índices al indicar el final no importará, funcionará igualmente (pero no es nada recomendable, no es buena práctica)
print(palabra.find("b",8,72))

#Método index(), funciona exactamente igual que el método find(), excepto cuando no se consigue el elemento buscado, en lugar de -1 nos da un error indicando que no se encontró la subcadena
frase = "Mi perro es gris con negro y amarillo"
print(frase.index("perro"))
print(frase.index("o"))
print(frase.index("rro es gris"))

palabra ="hipopotomonstruoesquipedaliofobia"
print(palabra.index("b",8,32))

print(palabra.index("b",8))

print(palabra.index("b",8,72))

#Las siguiente líneas nos mostrará la diferencia entre find() e index(), si se descomentan las siguientes dos líneas y se colocan al comienzo crearán el error que solo se muestra con index() y no con find(), y el programa se detendrá
nombre = "Benjamin"
#print(nombre.index("perro"))

#Método isalnum(), verifica que todos los caracteres de la cadena sea alfanuméricos
alfanumerico = "123456789abcdefg"
print(alfanumerico.isalnum())

no_alfanumerico="123456789asdfb.!"
print(no_alfanumerico.isalnum())

#Método isalpha(), verifica que todos los caracteres de la cadena sea alfabéticos
alfabetico = "abcdefghijk"
print(alfabetico.isalpha())

no_alfabetico = "abcdefghi234"
print(no_alfabetico.isalpha())

#Método isdecimal(), verifica que todos los caracteres de la cadena sean números
todo_num = "123456879"
print(todo_num.isdecimal())

no_todo_num = "123456879abcdefg"
print(no_todo_num.isdecimal())

#Los caracteres que necesitan tratamiento especial como los números para subíndice y superíndice no son considerados decimales
superindice = b = "\u00B2" #unicode for ²
print(superindice.isdecimal())

#Si el caracter en unicode no representa un número también retornará como resultado false
letra_unicode="\u0047" #unicode para G
print(letra_unicode.isdecimal())

#El nombre no hace referencia a que haya un número decimal, lo podemos comprobar si escribimos un número decimal en la cadena
decimal_comun = "1.5"
print(decimal_comun.isdecimal())

decimal_comun = "1,5"
print(decimal_comun.isdecimal())

#Método isdigit(), califica como true los números que conocemos y los números que necesitan un tratado especial como los que son utilizados como superíndice.

superindice = b = "\u00B2" #unicode para ²
print(superindice.isdigit())

todo_num = "123456789"
print(todo_num.isdigit())

no_todo_num = "123456789abcdefg"
print(no_todo_num.isdigit())

#Si el caracter en unicode no representa un número también retornará como resultado false
letra_unicode="\u0047" #unicode para G
print(letra_unicode.isdigit())

#Método lower y upper, retornan una copia de una cadena en mínúsculas y en mayúsculas respectivamente
texto_mayusculas = "HOLA MUNDO"
print(texto_mayusculas.lower())

texto_minusculas = "hola mundo"
print(texto_minusculas.upper())