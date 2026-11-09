meses = ["enero", "febrero", "marzo", "abril","mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
dia = int(input("dime el dia: "))
mes = input("dime el mes: ").lower()
hemisferio = ""
while dia > 31 or mes not in meses:
    dia = int(input("dime el dia: "))
    mes = input("dime el mes: ").lower()
while hemisferio != "norte" and hemisferio != "sur":
    hemisferio = input("dime el hemisferio norte/sur: ").lower()
if hemisferio == "norte":
    if dia >= 23 and mes == meses[8] or dia < 21 and mes == meses[11] or mes in meses[9:11]:
        print("otoño")
    elif  dia >= 21 and mes == meses[11] or dia < 21 and mes == meses[2] or mes in meses[0:2]:
        print("invierno")
    elif dia >= 21 and mes == meses[2] or dia < 21 and mes == meses[5] or mes in meses[3:5]:
        print("primavera")
    elif dia >= 21 and mes == meses[5] or dia < 23 and mes == meses[8] or mes in meses[6:8]:
        print("verano")
    else:
        print("no se en que epoca estás hulio")
if hemisferio == "sur":
    if dia >= 23 and mes == meses[8] or dia < 21 and mes == meses[11] or mes in meses[9:11]:
        print("primavera")
    elif  dia >= 21 and mes == meses[11] or dia < 21 and mes == meses[2] or mes in meses[0:2]:
        print("verano")
    elif dia >= 21 and mes == meses[2] or dia < 21 and mes == meses[5] or mes in meses[3:5]:
        print("otoño")
    elif dia >= 21 and mes == meses[5] or dia < 23 and mes == meses[8] or mes in meses[6:8]:
        print("invierno")  
    else:
        print("no se en que epoca estás hulio")