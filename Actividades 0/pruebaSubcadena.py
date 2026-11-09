nombreCompleto = input("Dame tu nombre y primer apellido: ")

nombre = nombreCompleto[:nombreCompleto.find(" ")]
apellido1 = nombreCompleto[1 + nombreCompleto.find(" "):]

#print(apellido1)
print("Tu nombre es "+ nombre + " y tu primer apellido es " + apellido1)