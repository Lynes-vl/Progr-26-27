num = int(input("Dame un nº: "))
fila = ""

if num < 3:
    for i in range(1, num+1):
        fila += "*"
    for i in range(1, num+1):
        print(fila)

else:
    const = num - 2
    fila1 = "*" + "#" * const + "*"
    fila2 = ""

    if num % 2 == 0:
        for i in range(num//2):
            if i % 2 == 0:
                fila2 += "*"
            elif i % 2 != 0:
                fila2 += "@"
        fila2 = fila2 + fila2[::-1]

    else:
        redon = int(num / 2 + 0.5)
        for i in range(redon):
            if i % 2 == 0:
                fila2 += "*"
            elif i % 2 != 0:
                fila2 += "@"
        z = fila2[:len(fila2) - 1]
        fila2 = fila2 + z[::-1] 

    if num % 2 == 0:
        if num//2 % 2 == 0:
            veces = num//2
            for i in range(veces):
                if i % 2 == 0:
                    print(fila1)
                else:
                    print(fila2)
            for i in range(veces):
                if i % 2 ==0:
                    print(fila2)
                else:
                    print(fila1)
        else:
            for i in range(num):
                if i % 2 ==0:
                    print(fila1)
                else:
                    print(fila2)
    else:
        for i in range(num):
            if i % 2 == 0:
                print(fila1)
            else:
                print(fila2)