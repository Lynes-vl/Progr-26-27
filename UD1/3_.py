bateria = int(input("¿Cuanta batería tiene?"))
conectado = input("¿Está conectado al cargador?")

if bateria < 20 and conectado == "no":
    print("Se activa el modo ahorro")

else:
    print("No se activa el modo ahorro")