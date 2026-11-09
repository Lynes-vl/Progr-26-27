num=int(input("Introduzca el número de árboles que va a introducir: "))
arbol=[]
x=0
for i in range(num):
    arbol.append(input("Tipo de árbol (A/B): ").upper())
    arbol.append(int(input("Diámetro del árbol (m): ")))
    arbol.append(int(input("Altura del árbol (m): ")))
    if arbol[x]=="B":
        arbol.append(int(input("Edad del árbol (años): ")))
        print(arbol[x : x+4])
        x+=4
    else:
        print(arbol[x : x+3])
        x+=3
x=0
altura=[]
anios=[]
for i in range(num):
    altura.append(arbol[x+2])
    if arbol[x]=="A":
        x+=3
    else:
        anios.append(arbol[x+3])
        x+=4
alMa=altura[0]
alMi=altura[0]
m30=0
for i in altura:
    if i>alMa:
        alMa=i
    elif i<alMi:
        alMi=i
    if i>30:
        m30+=1
pos=2
x=0
while arbol[pos]!=alMa:
    if arbol[x]=="A":
        x+=3
        pos+=3
    else:
        x+=4
        pos+=4
pos-=2
media=1
for i in anios:
    media+=i
media = media // len(anios)
print(f"La altura máxima es {alMa} m.")
print(f"La altura mínima es {alMi} m.")
print(f"La media de edad para los de tipo B es {media} años.")
print(f"Existen {m30} árboles en total de más de 30 m.")

print("Datos del árbol con altura máxima:")
if arbol[pos] == "A":
    print(arbol[pos:pos+3])
else:
    print(arbol[pos:pos+4])
x=0
print("Todos los árboles:")
for i in range(num):
    if arbol[x]=="A":
        print(arbol[x : x+3])
        x+=3
    else:
        print(arbol[x : x+4])
        x+=4
    