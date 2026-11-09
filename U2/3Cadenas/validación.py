cadena = input("Dame una cadena que empiece por A: ").upper()
# Validar que cadena empieza por mayuscula SI no volver a leer cadena
while cadena[0] != "A":
    cadena = input("Dame una cadena que empiece por A: ").upper()
print(len(cadena))