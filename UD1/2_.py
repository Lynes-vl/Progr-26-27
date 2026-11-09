edad = int(input("¿Cuantos años tienes?"))

if edad >= 16:
    print("Se permite comprar el juego")

else:
    autorizacion = input("¿Un adulto dio autorización parental desde la cuenta familiar?")

    if autorizacion == "si":
        print("Se permite comprar el juego")

    else:
        print("No se permite comprar el juego")