operar = input("""========================================
	CALCULADORA
========================================
Introduzca + si desea sumar
Introduzca - si desea restar
Introduzca * si desea multiplicar
Introduzca / si desea dividir
:""")
x = int(input("Dime un número: "))
y = int(input("Dime otro número: "))
match operar:
    case "+":
        print(x+y)
    case "-":
        print(x-y)
    case "*":
        print(x*y)
    case "/":
        print(x/y)