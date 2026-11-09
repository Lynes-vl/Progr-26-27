importar = float(input("¿Cuanto dinero quieres enviar?: "))
hoy = float(input("¿Cuanto dinero ya has enviado hoy?: "))

if importar >= 0.50 and importar <= 1000 and not(importar + hoy > 2000):
    print("Puedes enviar dinero")

else:
    print("No puedes enviar dinero")