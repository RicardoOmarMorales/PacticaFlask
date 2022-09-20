#Desafío 8 reinas
#Armamos el tablero
tablero = [0,1,2,3,4,5,6,7]
fila = 0
while fila < 8:
    columna = 0
    while columna < 8:
        if tablero[columna] == fila:
            print(" R ", end = "")
        else:
            print(" . ", end = "")
        columna +=1
    print()
    fila += 1





