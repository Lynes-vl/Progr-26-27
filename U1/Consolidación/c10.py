num = int(input("Dame un nº: "))
x = y = 1
fin = z = 0
for i in range(len(str(num))):
    x = 10 * x
    div = num // x
    div = div * x
    fin = num - div
    prin = fin // (x //10)
    z = prin + z
print(z)