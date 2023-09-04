#Con la siguiente sentencia creamos un archivo o reemplazamos todo el contenido de un un archivo determinado (no dejaré el archivo creado, para que se cree, y luego se debe ejecutar el archivo .py 26 para probar la sentencia with para agregar contenido al final de dicho archivo), el archivo se crea en la misma carpeta en donde se creó el archivo .py

notas = {
    "Nora": 87,
    "Gino": 100,
    "Loretto": 67,
    "Talina": 45
}

with open("data_estudiantes.txt", "w") as archivo:
    for nombre, nota in notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")
