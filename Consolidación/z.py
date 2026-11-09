num = int(input("Dame un nº: "))
for i in range(1, num +1):
    fila = ""
    if i == 1 or i == num:
        for i in range(num):
            fila = fila + "*"
        print(fila)
    else:
        fila = "*"
        for i in range(num - 2):
            fila = fila + " "
        fila = fila + "*"
        print(fila)