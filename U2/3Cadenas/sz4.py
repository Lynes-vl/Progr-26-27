anio = int(input("Dime un año: "))
while anio>0:
    if anio % 4 == 0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
    anio = input("Dime un año: ")