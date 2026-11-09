edad = input(input("Edad del usuario: "))
saldo = float(input("Saldo del usuario"))
bateria = int(input("Batería del patinete"))

if edad >= 18 and saldo >= 1 and bateria > 15:
    desbloquearPatinete = True
else:
    desbloquearPatinete = False
print(desbloquearPatinete)