#Apartado A
j1=[]
j2=[]
x=input("Elije pares o nones: ").lower()
while x!="pares" and x!="nones":
    print("Valor incorrecto")
    x=input("Elije pares o nones: ").lower()
j1.append(x)
if x=="pares":
    j2.append("nones")
else:
    j2.append("pares")
x=int(input("cuántos dedos apuesta el jugador 1: "))
while x<0 or x>5:
    print("Valor incorrecto")
    x=int(input("cuántos dedos apuesta el jugador 1: "))
j1.append(x)
x=int(input("cuántos dedos apuesta el jugador 2: "))
while x<0 or x>5:
    print("Valor incorrecto")
    x=int(input("cuántos dedos apuesta el jugador 2: "))
j2.append(x)
if (j1[1]+j2[1])%2==0:
    win="pares"
else:
    win="nones"
if win in j1:
    ganador="1"
else:
    ganador="2"
print(f"Gana es el jugador {ganador}")
