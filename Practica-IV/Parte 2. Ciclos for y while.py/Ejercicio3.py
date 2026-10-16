#Escribe un programa que genere un número aleatorio1 entre 1 y 100 y pida al usuario que lo adivine.
import random
secreto= random.randint(1, 100)
intento= 0
intentos= 0
while intento != secreto:
    intento = int(input("Adivina el numero entre 1 y 100: "))
    intentos += 1
    if intento < secreto:
        print("Muy bajo, prueba un numero mayor.")
    elif intento > secreto:
        print("Muy alto, prueba un numero menor.")

print("¡Correcto! Lo adivinaste en ", intentos, "intentos.")
print(secreto)
 