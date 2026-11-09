dia = input("día de la semana: ")
dia = dia.upper()
if dia == "LUNES":
    print("===================")
    print("         LUNES     ")
    print("===================")
    print("8-9 FOL")
    print("9-10 EDE")
    print("10-11 PROG")
    print("11-11:30 Recreo")
    print("11:30-12 Progr")
    print("12-14 BBDD")
    print("===================")
elif dia == "SÁBADO" or dia == "DOMINGO":
    print("Día de estudio y reflexión")
else:
    print("Valor incorrecto")