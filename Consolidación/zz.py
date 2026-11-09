num = int(input("Dame un nº: "))
for i in range(1, num +1):
    if i == 1 or i == num:
        fila = ""
        for i in range(num):
            fila = fila + "*"
        print(fila)
    else:
        fila2 = "*"
        for i in range(num - 2):
            fila2 = fila2 + " "
        fila2 = fila2 + "*"
        print(fila2)