num = int(input("Dame un nº: "))
fila = ""
# Cuadros 1-2u^2
if num < 3:
    for i in range(1, num+1):
        fila += "*"
    for i in range(1, num+1):
        print(fila)
# Cuadros mayores a 2u^2
else:
    const = num - 2
    fila1 = "*" + "#" * const + "*" #Techo y suelo
    fila2 = ""
# Cuadros pares
    if num % 2 == 0:
        for i in range(num//2): #Guardo la mitad de la lifa media
            if i % 2 == 0:
                fila2 += "*"
            elif i % 2 != 0:
                fila2 += "@"
        fila2 = fila2 + fila2[::-1] #Guardo la fila media con su mitad más la otra mitad alrevés para que quede simétrico
# Cuadros inpares
    elif num % 2 != 0:
        num = int(num / 2 + 0.5) #Redondeo la división al por mayor sin usar la biblioteca de matemáticas para tener la mitad y el centro
        for i in range(num): #Saco la mitad y el centro de la fila
            if i % 2 == 0:
                fila2 += "*"
            elif i % 2 != 0:
                fila2 += "@"
        z = fila2[:len(fila2) - 1] # Duplico lo que saqué sin el centro y le doy la vuelta para que quede impar
        fila2 = fila2 + z[::-1] #Uno la primera parte con el centro + la otra parte
# Imprimo todo
    print(fila1)
    for i in range(const):
        print(fila2)
    print(fila1)

