num=int(input("Introduzca el número de árboles que va a introducir: "))
tipo=[]
diametro=[]
altura=[]
edad=[]
for i in range(num):
    tipo.append(input("Tipo de arbol (A/B): ").upper())
    diametro.append(int(input("Diámetro del arbol (m): ")))
    altura.append(int(input("Altura del arbol (m): ")))
    if tipo[i] == "B":
        edad.append(int(input("Edad del arbol (años): ")))
    else:
        edad.append("Null")
    if tipo[i] == "A":
        print(f"Tipo{tipo[i]}, {diametro[i]}, {altura[i]}")
    else:
        print(f"Tipo{tipo[i]}, {diametro[i]}, {altura[i]}, {edad[i]}")
alturaMa=altura[0]
alturaMi=altura[0]
for h in altura:
    if h>alturaMa:
        alturaMa=h
    elif h<alturaMi:
        alturaMi=h
media=1
for i in edad!="Null":
    media=media*i/2
arM30=0
for i in altura:
    if i >30:
        arM30+=1
print(f"La altura máxima es {alturaMa} m.")
print(f"La altura mínima es {alturaMi} m.")
print(f"La media de edad para los de tipo B es {media} años")
print(f"Existen {arM30} árboles en total de más de 30 m. ")

 
for i in range(num):
    if tipo[i] == "A":
        print(f"Tipo{tipo[i]}, {diametro[i]}, {altura[i]}")
    else:
        print(f"Tipo{tipo[i]}, {diametro[i]}, {altura[i]}, {edad[i]}")