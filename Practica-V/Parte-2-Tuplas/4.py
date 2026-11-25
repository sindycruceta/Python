#Este algoritmo pide al usuario textos separados por comas y devuelve una cadena de textos separados por espacios
entrada = input("Ingresa textos separados por comas: ")

elementos = entrada.split(",")

#Bucle for para pasar los elementos a una nueva lista
lista = []
for elemento in elementos:
    lista.append(elemento)

#Convertimos la lista en una tupla
tupla = tuple(lista)

#Convertimos la tupla en una única cadena separada por un espacio
resultado = " ".join(tupla)

print("\nTupla generada:", tupla)
print("Cadena final:", resultado)
