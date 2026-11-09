gasto = int(input("¿Cuanto dinero ha gastado el cliente?: $"))

if gasto > 100:
    print("El cliente es elegible para el descuento")

else:
    programa = input("¿El cliente es miembro del programa de lealtad?: ")

    if programa == "si":
        print("El cliente es elegible para el descuento")

    if programa == "no":
        print("El cliente no es elegible para el descuento")