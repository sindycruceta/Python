#Este programa solicita al usuario una cantidad de números a ingresar y crea dos listas, para luego sumarlas. 

numeros_ingresar = int(input("¿Cuántos números desea ingresar en cada lista? "))

lista_1 = []
lista_2 = []
resultado = []

i = 0

print("-----------LISTA 1-----------");
while i < numeros_ingresar:
    valor = int(input(f"Ingrese el número para la posición {i}: "))
    lista_1.append(valor)
    i += 1

i = 0

print("-----------LISTA 2-----------");
while i < numeros_ingresar:
    valor = int(input(f"Ingrese el número para la posición {i}: "))
    lista_2.append(valor)
    i += 1

i = 0
while i < numeros_ingresar:
    suma = lista_1[i] + lista_2[i]
    resultado.append(suma)
    i += 1

print("\n");
print("--- Resultados ---")
print("Lista 1:", lista_1)
print("Lista 2:", lista_2)
print("Suma:", resultado)
