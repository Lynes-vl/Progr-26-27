puntos = int(input("¿Cuantos puntos ha obtenido?: "))
vidas = int(input("¿Cuantas vidas le quedan?: "))

if puntos >= 1000 and vidas >= 1:
    print("Pasa al siguiente nivel")

else:
    print("No pasa al siguiente nivel")