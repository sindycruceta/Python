#Primero le pedimos los numeros al usuario:
texto1= input("Ingrese los numeros: ")

#Ahora separo los numeros
mi_texto1= texto1.split(",")

#Creo una lista vacia
lista1=[]

for x in mi_texto1:
    lista1.append(int(x))
tuple(lista1)
    
#Ahora hago lo mismo pero con la segunda lista
texto2= input("Ingrese los numeros: ")

#Ahora separo los numeros
mi_texto2= texto2.split(",")

#Creo una lista vacia
lista2=[]

for x in mi_texto2:
    lista2.append(int(x))
tuple(lista2) 

#Concatenar
tupla3= lista1 + lista2

#Imprimo el resultado
print(tupla3)