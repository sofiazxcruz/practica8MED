# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as file:
    # Lee todas las líneas del archivo en una lista
    lines = file.readlines()

# Muestra cada línea del archivo
for line in lines:
    print(line.strip())
