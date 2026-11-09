animales = ["gato", "perro", "elefante", "pingüino", "zorro", "lobo"]
x = input("escribe el nombre de un animal: ")
encontrado = False
ps = 0
while not encontrado and ps < len(animales):
    if x == animales[ps]:
        encontrado = True
    else:
        ps = ps + 1
if encontrado:
    print("El", x,"sí está en la lista")
else:
    print("El", x,"no está en la lista")