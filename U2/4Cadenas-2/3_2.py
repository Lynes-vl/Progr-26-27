bucle = True
msj = "Imagina que tienes dos vacas"
while bucle:
    print("==========================================================================")
    print(msj)
    print("Introduzca 1 si desea ver carácter a carácter")
    print("Introduzca dos si desea saber el % de veces que aparece en una la cadena")
    print("Escriba exit si desea terminar el programa")
    print("==========================================================================")
    option = input()
    while option != "1" and option != "dos" and option != "exit":
        print("Opción incorrecta")
        print("==========================================================================")
        print(msj)
        print("Introduzca 1 si desea ver carácter a carácter")
        print("Introduzca dos si desea saber el % de veces que aparece en una la cadena")
        print("Escriba exit si desea terminar el programa")
        print("==========================================================================")
        option = input()
    cont=0
    match option:
        case "1":
            print("Seleccionada opción de menú 1")
            msj = input("Dame una frase: ")
            for i in msj:
                print(i)
        case "dos":
            print("Seleccionada opción de menú 2")
            letr = input("Dime una letra que buscar en la frase: ")
            for i in msj:
                if i == letr:
                    cont+=1
            print("Se repite la letra \"" +str(letr) +"\"", cont, "veces")
        case "exit":
            bucle = False
print("Fin")