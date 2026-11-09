import random

x = random.randint(0, 4)
y = random.randint(0, 4)
resultado = x + y

respuesta = int(input(f"Introduce el resultado: {x} + {y} = "))

while respuesta != resultado:
    respuesta = int(input(f"Introduce el resultado: {x} + {y} = "))
