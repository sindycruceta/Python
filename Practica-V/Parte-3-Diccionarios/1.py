cantidad=int(input("Cuantas personas desea ingresar? "))
personas={}
for i in range(cantidad):
    nombre=input("Ingrese el nombre de la persona: ")
    edad= int(input("Ingrese la edad de la persona: "))
    personas[nombre]= edad
print(personas)