#Este algoritmo pide al usuario una cantidad de números y calcula la suma de todos los números ingresados.
numeros = [];
cantidad=int(input("Ingrese la cantidad de números que desea ingresar: "));
for i in range(cantidad):
    numero=int(input("Ingrese un número: "));
    numeros.append(numero);
    if numero < 0:
        print("Se ha ingresado un número negativo. Se detendrá la entrada de números.");
        break;
    
print("Los números ingresados son:", numeros);
print("La suma de los números ingresados es:", sum(numeros));
