x = int(input("Dame un nº: "))
y = int(input("Dame otro nº: "))

if x >= 0 and y >= 0:
    print("Dijiste dos nº positivos")
elif x < 0 and y < 0:
    print("No dijiste nº positivos")
else:
    print("Dijiste un nº positivo")