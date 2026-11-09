coste = 0.0
precio = 0.0
while coste >= 0:
    precio += coste
    coste = float(input("Introduce el precio: "))
print("El precio total es:", precio, "€")