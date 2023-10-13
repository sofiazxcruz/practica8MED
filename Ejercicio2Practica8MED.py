nombres = []
while True:
    nombre = input("Ingrese un nombre (o escriba 'fin' para terminar): ")
    if nombre == "fin":
        break
    nombres.append(nombre)

with open("nombres.txt", "w") as archivo:
    archivo.write('\n'.join(nombres))
