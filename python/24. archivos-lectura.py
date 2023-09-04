#Con la siguiente sentencia iteraremos sobre cada línea del archivo de texto frases_ famosas.txt (el archivo debe abrirse y ejecutarse con el idle de python para que funcione)

with open("frases_famosas.txt") as archivo:
    for linea in archivo:
        print("===línea===")
        print(linea)