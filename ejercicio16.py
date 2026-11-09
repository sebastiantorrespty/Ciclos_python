suma=0 
cantidad=0
nota = float(input("Ingrese una nota (o -1 para terminar): "))
while nota != -1:
    suma += nota
    cantidad += 1
    nota = float(input("Ingrese una nota (o -1 para terminar): "))
if cantidad > 0:
    promedio = suma / cantidad
    promfinal = round(promedio, 1)
    print(f"El promedio es: {promfinal}")
else:
    print("No se ingresaron notas.")