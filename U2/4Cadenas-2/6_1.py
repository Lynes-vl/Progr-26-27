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