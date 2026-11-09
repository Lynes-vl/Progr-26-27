text="La inyección de SQL es un tipo de ciberataque encubierto en el cual un hacker inserta código propio en un sitio web con el fin de quebrantar las medidas de seguridad y acceder a datos protegidos. Una vez dentro, puede controlar la base de datos del sitio web y secuestrar la información de los usuarios. Le explicamos cómo funcionan los ataques de inyección de SQL, cómo combatirlos y cómo una herramienta antivirus potente lo puede proteger contra las consecuencias."
opcion=""
opciones=["A", "B", "C", "D", "9999"]
while opcion!="9999":
    print("""Pulsa A si deseas ver las frases separadas
Pulsa B si deseas saber cuántas frases hay. 
Pulsa C si deseas saber cuántas palabras hay.
Pulsa D si deseas saber cuántas palabras tiene cada frase.""")
    opcion=input().upper()
    while opcion not in opciones:
        print("""Pulsa A si deseas ver las frases separadas
Pulsa B si deseas saber cuántas frases hay. 
Pulsa C si deseas saber cuántas palabras hay.
Pulsa D si deseas saber cuántas palabras tiene cada frase.""")
        opcion=input().upper()
    print(f"Opción {opcion} elegida")
    x=". "
    match opcion:
        case "A":
            
            text=text.split(x)
            for i in range(len(text)-1):
                print(text[i]+".")
                print()
            print(text[len(text)-1])
        case "B":
            text=text.split(x)
            print(f"Hay {len(text)} frases.")
        case "C":
            text=text.split()
            print(f"Hay {len(text)} palabras.")
        case "D":
            text=text.split(x)
            for i in range(len(text)):
                print(f"Hay {len(text[i].split())} en la frase {i+1}")