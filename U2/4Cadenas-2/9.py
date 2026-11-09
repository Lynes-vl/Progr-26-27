num = "3456178935471105641"
pos = 0
numF = ""
for i in num[::-1]:
    if pos % 3 ==0:
        numF = numF + "."
    numF+=i
    pos+=1
print(numF[::-1])