num = int(input("Dame un nº: "))
x = 1
fin = 0
y = 1
for i in range(len(str(num))):
    x = 10 * x
    div = num // x
    div = div * x
    fin = num - div
    prin = fin // (x //10)
    print(prin)