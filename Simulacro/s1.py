fin = True
while fin:
    grupos = []
    for i in range(1, 4):
        grupos.append(int(input(f"introduce{i}1º del grupo: ")))

    if grupos[0] < grupos[1] < grupos[2]:
        print("creciente")
    elif grupos[0] > grupos[1] > grupos[2]:
        print("decreciente")
    elif grupos[0] == 0 and grupos[1] == 0 and grupos[2] == 0:
        fin = False
    else:
        print("desordenado")
print("fin")