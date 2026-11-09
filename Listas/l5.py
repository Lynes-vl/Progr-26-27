import random
numeros = []
cuadrados = []
cubos = []
aDos = 1
aTres = 1
for i in range(20):
    numeros.append(random.randint(0, 100))
    cuadrados.append(numeros[i] *numeros[i])
    cubos.append(cuadrados[i] *numeros[i])
print(numeros)
print(cuadrados)
print(cubos)