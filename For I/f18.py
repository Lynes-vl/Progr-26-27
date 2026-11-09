num = int(input("Dime un número: "))
calc = 1
for i in range(num, 0, -1):
    calc = calc * i
print(f"{num}! = {calc}")
#print(num,"! =",calc)