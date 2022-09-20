#INGRESO DE DATOS
#Perímetro
while True:
    try:
        triangulo_lado1 = int(input("Ingrese medida del primer lado: "))
        triangulo_lado2 = int(input("Ingrese medida del segundo lado: "))
        triangulo_lado3 = int(input("Ingrese medida del tercer lado: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if triangulo_lado1 < 0:
        print("Debes escribir un número positivo.")
        continue
    if triangulo_lado2 < 0:
        print("Debes escribir un número positivo.")
        continue
    if triangulo_lado3 < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

triangulo_perimetro=triangulo_lado1+triangulo_lado2+triangulo_lado3
print("El perímetro del triángulo es:" + str(triangulo_perimetro))


#Superficie
while True:
    try:
        triangulo_base = int(input("Ingrese medida de la base: "))
        triangulo_altura = int(input("Ingrese medida de la altura: "))
        
    except ValueError:
        print("Debes escribir un número.")
        continue

    if triangulo_base < 0:
        print("Debes escribir un número positivo.")
        continue
    if triangulo_altura < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

triangulo_superficie=(triangulo_base*triangulo_altura)/2
print("La superficie del triángulo es: " + str(triangulo_superficie))
