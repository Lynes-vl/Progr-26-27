x = []
for i in range(10):
    x.append(int(input("introduce un nº: ")))
mini = x[0]
maxi =  x[0]
for i in range(len(x)):
    if mini >= x[i]:
        mini = x[i]
    if maxi <= x[i]:
        maxi = x[i]
print(maxi)
print(mini)