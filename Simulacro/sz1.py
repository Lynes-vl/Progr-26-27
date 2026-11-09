nom = input("Introduce el nombre de un alumno: ")
while nom != "exit":
    nota = int(input("Introduce la nota de 0 al 100: "))
    while nota <0 or nota >100:
        nota = int(input("Introduce la nota de 0 al 100: "))
    if nota>=90:
        print("Sobresaliente")
    elif nota>=70 and nota<=89:
        print("Notable")
    elif nota>=60 and nota<=69:
        print("Bien")
    elif nota>=50 and nota<=59:
        print("Suficiente")
    else:
        print("Suspenso")
    nom = input("Introduce el nombre de un alumno: ")
