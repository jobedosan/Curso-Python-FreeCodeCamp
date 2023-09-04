#El siguiente código agrega contenido al archivo creado con el archivo 25

nuevas_notas = {
    "Emily" : 54,
    "Daniel": 98,
    "Julienne": 78
}

with open("data_estudiantes.txt", "a") as archivo:
    for nombre, nota in nuevas_notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")