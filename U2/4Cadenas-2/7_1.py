nom=input("Dame un nombre y dos apellidos: ")
nom=nom.split()
print(nom[1][0].upper()+nom[1][1:], nom[2][0].upper()+nom[2][1:], nom[0][0].upper()+nom[0][1:])