#Este algoritmo pide al usuario un número y calcula la suma de todos los números del 1 hasta ese número.

numero= int(input("Ingrese un número: "));
suma=0;

for i in range(1, numero+1):
    suma += i;
print("La suma de los números del 1 al", numero, "es:", suma);