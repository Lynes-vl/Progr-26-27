san1 = input("Introduce el grupo sanguineo1: ")
san2 = input("Introduce el grupo sanguineo2: ")
rh1 = input("Introduce el RH de 1: ")
rh2 = input("Introducel el RH de 2: ")
listaDonaA=["A", "AB"]
listaRecibeA=["A", "0"]
listaDonaB=["B", "AB"]
listaRecibeB=["B", "0"]
listaDonaAB=["AB"]
listaRecibeAB=["A", "B", "AB", "0"]
listaDona0=["A", "B", "AB", "0"]
listaRecibe0=["0"]
listaDonaMas=["+"]
listaRecibeMas=["+", "-"]
listaDonaMenos=["+", "-"]
listaRecibeMenos=["-"]
if san1 == "A":
    if san2 in listaDonaA:
        if rh1 == "+":
            if rh2 in listaDonaMas:
                dona = True
    if san2 in listaRecibeA:
        if rh1 == "+":
            if rh2 in listaRecibeMenos:
                recibe = True
    
if san1 == "B":
    if san2 in listaDonaB:
        if rh1 == "+":
            if rh2 in listaDonaMas:
                dona = True
    if san2 in listaRecibeB:
        if rh1 == "+":
            if rh2 in listaRecibeMenos:
                recibe = True
if san1 == "AB":
    if san2 in listaDonaAB:
        if rh1 == "+":
            if rh2 in listaDonaMas:
                dona = True
    recibe = True
if san1 == "0":
    dona = True
    if san2 in listaRecibeA:
        if rh1 == "+":
            if rh2 in listaRecibeMenos:
                recibe = True