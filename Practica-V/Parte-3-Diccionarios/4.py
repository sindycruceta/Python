#Este programa solicita al usuario un texto y cuenta la frecuencia de cada letra, devuelve las letras encontradas alfabéticamente

texto = input('Ingrese un texto... ')
frecuencia = {}

for letra in set(texto):
    if letra == " ":
        continue
        
    cantidad = texto.count(letra)
    
    if cantidad > 0:
        frecuencia[letra] = cantidad

print(sorted(frecuencia));
