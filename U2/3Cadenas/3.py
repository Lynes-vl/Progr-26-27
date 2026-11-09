num = input("Dime un nº: ")
pos = len(num)-1
numB = ""
while pos>=0:
    numB = numB + num[pos]
    pos-=1
print(numB)