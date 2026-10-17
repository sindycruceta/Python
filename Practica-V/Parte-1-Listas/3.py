#Primero, le pido los datos al usuario
elementos= input("Ingrese los elementos que desee separados por comas: ")

#Aqui separé las palabras de la lista con .split 
elementos= elementos.split(",")

#Aqui cree una lista vacia
sin_repetidos=[]

#Aqui for recorre cada elemento de la lista
for x in elementos:
    
    #Aqui pregunta con if si el elemento todavía no está en la lista nueva
    if x not in sin_repetidos:
        
        #Aqui se agrega el nuemro elemento
        sin_repetidos.append(x)
        
#Imprimo el resultado
print(sin_repetidos)