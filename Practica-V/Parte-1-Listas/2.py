#Primero, le pido los datos al usuario
palabras= input("Ingrese una lista de palabras separadas por comas: ")
#Aqui separé las palabras de la lista con .split 
palabras= palabras.split(", ")
#Aquí con reversed da vuelta al orden y list lo convierte de nuevo en una lista normal que puedes imprimir
invertir= list(reversed(palabras))
#Por ultimo, imprimí la lista
print(invertir)