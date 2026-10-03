#Este algoritmo pide al usuario un número y muestra la tabla de multiplicar de ese número del 1 al 12.

numero = int(input("Ingrese un número: "));

for i in range(1,13):
    producto = numero * i;
    print(numero, "x", i, "=", producto);