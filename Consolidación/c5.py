num = int(input("Dame un nº: "))
fila = ""
if num < 3:
    for i in range(num):
        fila += "*"
    for i in range(num):
        print(fila)
else:
    const = num - 2
    fila1 = num * "*"
    fila2 = "*" + " " * const + "*"
    print(fila1)
    for i in range(const):
        print(fila2)
    print(fila1)