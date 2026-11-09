edades = []
alturas = []
media = 0.0
for i in range(1, 5):
    edades.append(int(input(f"Di la edad del alumon {i}: ")))
    alturas.append(float(input(f"Di la altura del alumon {i}: ")))
    media = media + float(alturas[i-1])

media = media / 4
print("Los alumnos mayores de edad son:")
for i in range(4):
    if float(edades[i]) >= 18:
        print("Alumno", i, ": ", edades[i], "años")
        if alturas[i] < media:
            print("Mide menos de la media")
print(media)
