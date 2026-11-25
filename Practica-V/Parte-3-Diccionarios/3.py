#Este algoritmo recibe los datos para crear dos diccionarios y crea uno nuevo a partir de ellos.

persona = {}
ocupacion = {}

nombre = input("Ingresa el nombre de la persona: ")
persona["nombre"] = nombre

puesto = input("Ingresa la ocupación de la persona: ")
ocupacion["puesto"] = puesto

diccionario_generado = persona | ocupacion

print("\nDiccionario final combinado:")
print(diccionario_generado);
