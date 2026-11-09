premiun = input("¿Tiene un plan Premiun? (S/N): ")
premiun = premiun.upper()

velocidad = int(input("¿Cuanta velocidad de conexión tiene?(Mbps): "))

if premiun == "S" and velocidad > 25:
    ver4K = True
else:
    ver4K = False
print(ver4K)
