edad = int(input("¿Cuantos años tienes?: "))
ciudadanía = input("¿Eres ciudadano del país? si o no: ")

if edad >= 18 and str(ciudadanía) == "si":
    print("Puede presentarse a las elecciones locales")

else:
    print("No puede presentarse a las elecciones locales ")
