#Este programa solicita al usuario ingresar un número y devuelve la lista de números primos hasta determinado numero.
limite = int(input("Ingrese un número entero: "))

numeros_primos = []

for num in range(2, limite + 1):
    es_primo = True 
    

    for i in range(2, num):
        if num % i == 0:
            es_primo = False  
            break  
            
        numeros_primos.append(num)

# 5. Imprimimos el resultado final
print("Los números primos hasta el", limite, "son:")
print(numeros_primos)
