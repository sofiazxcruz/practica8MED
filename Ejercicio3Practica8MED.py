file_path = "archivo_inexistente.txt"

if not os.path.exists(file_path):
    print("El archivo no se encuentra.")
else:
    with open(file_path, "r") as file:
        content = file.read()
