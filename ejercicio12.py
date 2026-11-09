numero=7 
intento = int(input("Adivina el numero entre el 1 y el 10: "))
while intento != numero:
    if intento < numero:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    intento = int(input("Intenta de nuevo: "))
print("Adivinaste el numero.")
