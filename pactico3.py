#**Ejercicio 3**

#Estamos en un caampeonato en la primera ronda, somos 3 equipos y necesitamos determinar la posición de cada uno de acuerdo al resultado (en goles) de cada partido. 
#Por ejemplo, los equipos son A,B y C. En la primera ronda juegan: AB - AC - BC.

#PRIMER PARTIDO
print ("PRIMER PARTIDO - EQUIPO A vs EQUIPO B")
equipoA = int(input("Ingresa los goles del Equipo A: "))
equipoB = int(input("Ingresa los goles del Equipo B: "))
goles_equipoA = equipoA
goles_equipoB = equipoB
print ("SEGUNDO PARTIDO - EQUIPO A vs EQUIPO C")
equipoA = int(input("Ingresa los goles del Equipo A: "))
equipoC = int(input("Ingresa los goles del Equipo C: "))
goles_equipoA = goles_equipoA + equipoA
goles_equipoC = equipoC
print("TERCER PARTIDO - EQUIPO B vs EQUIPO C")
equipoB = int(input("Ingresa los goles del Equipo B: "))
equipoC = int(input("Ingresa los goles del Equipo C: "))
goles_equipoB = goles_equipoB + equipoB
goles_equipoC = goles_equipoC + equipoC

print("Goles A: " + str(goles_equipoA))
print("Goles B: " + str(goles_equipoB))
print("Goles C: " + str(goles_equipoC))

if goles_equipoA > goles_equipoB:
    if goles_equipoA > goles_equipoC:
        print("Primero EQUIPO A")
elif goles_equipoB > goles_equipoA:
    if goles_equipoB > goles_equipoC:
        print("Primero EQUIPO B")
elif goles_equipoC > goles_equipoA:
    if goles_equipoC > goles_equipoB:
        print("Primero EQUIPO C")



