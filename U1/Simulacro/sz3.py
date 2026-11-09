dias=[0,31,28,31,30,31,30,31,31,30,31,30]
xMes = int(input("introduce el mes en nº: "))
xDia = int(input("introduce el día del mes: "))
diasTras = 0
for i in dias[:xMes]:
    diasTras += diasTras+i
diasTras = diasTras + xDia
print("han pasado",diasTras,"días desde el 1 de Enero")