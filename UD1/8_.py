cuota = input("¿Mantiene la cuota al día?(S/N): ")
reserva = input("¿Tienes reserva?(S/N): ")

cuota = cuota.upper()
reserva = reserva.upper()

if cuota == "S" and reserva == "S":
    print("Puedes entrar a la sala de Spinning")

else:
    print("No puedes entrar a la sala de Spinning")
