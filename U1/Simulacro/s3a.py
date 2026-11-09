san1 = input("Introduce un grupo sanguineo: ")
san2 = input("Introduce otro grupo sanguineo: ")
listaDonaA=["A", "AB"]
listaRecibeA=["A", "0"]
listaDonaB=["B", "AB"]
listaRecibeB=["B", "0"]
listaDonaAB=["AB"]
listaRecibeAB=["A", "B", "AB", "0"]
listaDona0=["A", "B", "AB", "0"]
listaRecibe0=["0"]
if san1 == "A":
    if san2 in listaDonaA:
        dona = True
    if san2 in listaRecibeA:
        recibe = True
if san1 == "B":
    if san2 in listaDonaB:
        dona = True
    if san2 in listaRecibeB:
        recibe = True
if san1 == "AB":
    if san2 in listaDonaAB:
        dona = True
    recibe = True
if san1 == "0":
    dona = True
    if san2 in listaRecibeA:
        recibe = True