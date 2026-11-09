x = int(input("Dime un número: "))

match x:
    case 0:
        print("CERO")
    case 1:
        print("UNO")
    case 2:
        print("DOS")
    case _:
        print("OTRAS")