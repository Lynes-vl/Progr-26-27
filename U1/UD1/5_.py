precio = int(input("¿Cuanto cuesta el pedido?: "))
suscripcion = input("¿Tienes la suscribción Plus?(S/N): ")

suscripcion = suscripcion.upper()

if precio >= 35 or suscripcion == "S":
    print("No se cobran gastos de envío")

else:
    print("Se cobran gastos de envío")