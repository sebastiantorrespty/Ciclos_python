vocales=0 
palabra=input("Ingrese una palabra: ")
for letra in palabra:
    if letra in "aeiouAEIOU":
        vocales+=1
print(f"La palabra \"{palabra}\" tiene {vocales} vocales.")
