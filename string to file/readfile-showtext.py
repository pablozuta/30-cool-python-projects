# abrir el archivo en read mode
with open("output.txt", "r") as file:
    # leer el contenido del archivo y guardarlo en una variable
    file_content = file.read()

    # mostrar el contenido por consola
    print(file_content)