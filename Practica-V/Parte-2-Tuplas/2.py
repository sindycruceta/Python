#Pedir datos al usuario
texto1= input("Ingrese los elementos que desee: ")

#Ahora separo los datos
mi_texto1= texto1.split(",")

#Creo una lista vacia
lista1=[]
#Recorro cada elemento y lo agrego a la lista
for x in mi_texto1:
    lista1.append(x)
#Convierto la lista en una tupla
tupla1=tuple(lista1)

#Ahora hago lo mismo pero con la segunda lista
#Pedir datos al usuario
texto2= input("Ingrese los elementos que desee: ")

#Ahora separo los datos
mi_texto2= texto2.split(",")

#Creo una lista vacia
lista2=[]
#Recorro cada elemento y lo agrego a la lista
for x in mi_texto2:
    lista2.append(x)
#Convierto la lista en una tupla
tupla2=tuple(lista2)

#Creo una lista vacía para guardar los elementos comunes
comunes=[]
#Recorro la primera tupla elemento por elemento
for x in tupla1:
    #Si el elemento está en la segunda tupla y todavía no lo guardé, lo agrego
    if x in tupla2 and x not in comunes:
        comunes.append(x)
#Convierto la lista de comunes en una tupla
resultado= tuple(comunes)
#Imprimo el resultado
print(resultado)