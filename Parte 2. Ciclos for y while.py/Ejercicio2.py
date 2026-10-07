#Este algoritmo pide al usuario un número y calcula la suma de todos los números del 1 hasta ese número.

numero = int(input("Ingrese un número: "))
suma = 0

if numero < 1:
    print("El número ingresado no es válido. Por favor ingrese un número mayor o igual a 1.")
else:
    for i in range(1, numero + 1):
        suma += i
    print("La suma de los números del 1 al", numero, "es:", suma)