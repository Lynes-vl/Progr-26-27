num = input("Dime un nº: ")
dig = int(input("Dime cuiantos digitos quieres quitarle desde la derecha: "))
numB = num[:len(num)-dig]
print(numB)