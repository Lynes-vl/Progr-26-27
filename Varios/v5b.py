num = int(input("Introduce en nº a elevar: "))
potencia = int(input("Introduce la potencia: "))
while num < 0 or potencia < 0:
    num = int(input("Introduce en nº a elevar: "))
    potencia = int(input("Introduce la potencia: "))
if potencia >1:
    for i in range(potencia-1):
        num = num * num
print("El resultado es:", num)