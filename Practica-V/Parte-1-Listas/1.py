#Pedir los numeros al usuario
texto=input("Ingrese los numeros separados por comas: ")
#Agrego .split para separar los numeros
lista= texto.split(",")

#Ahora creé una lista vacía
numeros=[]
#Agregue for para que recorra la lista y convierto cada numero a entero y lo agrego a numero
for x in lista:
    numeros.append(int(x))

#Ahora denomino las variables mayor y menor de los numeros
mayor= max(numeros)
menor= min(numeros)
#Imprimo el resultado
print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)