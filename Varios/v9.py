coste = 0.0
precio = 0.0
impuesto = 0.0
while coste >= 0:
    impuesto = coste * 7 / 100
    precio += coste + impuesto
    coste = float(input("Introduce el precio: "))
print("El precio total es:", precio, "€")