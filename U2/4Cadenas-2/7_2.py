nom=input("Dame un nombre y dos apellidos: ")
nom=nom.split()
print(nom[1][0].upper()+nom[1][1:-1]+nom[1][len(nom[1])-1].upper(), nom[2][0].upper()+nom[2][1:-1]+nom[2][len(nom[2])-1].upper(), nom[0][0].upper()+nom[0][1:-1]+nom[0][len(nom[0])-1].upper())