precio = int(input("¿Cuanto cuesta el pedido?"))
cupon = input("¿Tiene un cupón activo?")

if precio > 20 and cupon == "si":
    print("Se aplica 10% de descuento")

else:
    print("No se aplica descuento")