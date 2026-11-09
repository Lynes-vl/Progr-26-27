pulseraVIP = input("¿Tene pulsera VIP? (S/N): ")
pulseraVIP = pulseraVIP.upper()
entradaBird = input("¿Tiene entrada early Bird? (S/N): ")
entradaBird = entradaBird.upper()
puntos = int(input("Puntos canjeados: "))

if pulseraVIP == "S" or entradaBird == "S" and puntos >= 500:
    entrarZonaVIP = True
else:
    entrarZonaVIP = False
print(entrarZonaVIP)