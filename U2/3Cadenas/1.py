num = input("Introduce un nº: ")
capicua = False
if num == num[len(num):-1:-1]:
    capicua = True
print(capicua)