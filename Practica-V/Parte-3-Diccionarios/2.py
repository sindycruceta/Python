# Pido cuántas personas va a ingresar y lo convierto a número
cantidad=int(input("Cuantas personas desea ingresar? "))

# Creo un diccionario vacío para guardar los datos
personas={}

# Repito el proceso según la cantidad de personas
for i in range(cantidad):
        # Pido el nombre de la persona
    nombre=input("Ingrese el nombre de la persona: ")
        # Pido la edad y la convierto a número
    edad= int(input("Ingrese la edad de la persona: "))
        # Guardo el nombre como clave y la edad como valor
    personas[nombre]= edad
# Imprimo el diccionario
print(personas)

texto=input("Ingrese el nombre de la persona a eliminar: ")
if texto in personas:
    del personas[texto]
else:
    print("Esa persona no existe")
print(personas)