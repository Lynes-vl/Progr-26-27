cadena=input("Dame una cadena: ")
carac=input("Dame dos caracteres: ")
while len(carac)>2:
    print("Longitud incorrecta")
    carac=input("Dame dos caracteres: ")
print(cadena.replace(carac[0], carac[1]))