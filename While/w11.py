import random
num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
#suma = int(input(f"{num1}+{num2}="))
suma = int(input(str(num1) + "+" + str(num2) + "="))

while suma != num1 + num2:
    #suma = int(input(f"{num1}+{num2}="))
    suma = int(input(str(num1) + "+" + str(num2) + "="))