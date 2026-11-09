bucle = True
num = []
creciente = True
decreciente = True
while bucle:
    x = int(input("introduce un nº: "))
    if x != 0:
        num.append(x)
    else:
        bucle = False
i = 0
while i < len(num) - 1 and creciente == True or decreciente == True:
    if num[i] < num[i + 1]:
        decreciente = False
    elif num[i] > num[i + 1]:
        creciente = False
    i += 1
if creciente:
    print("creciente")
elif decreciente:
    print("decreciente")
else:
    print("desordenada")