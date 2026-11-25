# 1. Este programa recibe los nombres y edades ingresados por el usuario y devuelve una lista de tuplas con los valores
nombres = []
edades = []

total_personas = int(input("¿Cuántas personas deseas registrar?: "))

i = 0  
while i < total_personas:
    print(f"\n--- Persona {i+1} ---")
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    
    nombres.append(nombre)
    edades.append(edad)
    
    i += 1  

lista_de_tuplas = []
j = 0 
while j < total_personas:
    persona = (nombres[j], edades[j])
    lista_de_tuplas.append(persona)
    
    j += 1  

print("\nLista de tuplas resultante:")
print(lista_de_tuplas)
