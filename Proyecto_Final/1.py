# Proyecto final de Sindy Cruceta y Helen Concepcion: Gestor de contactos.
opciones= [1,2,3,4,5,6,0]
contactos= []
def mostrar_menu():
    print("===================================================")
    print("Te damos la bienvenida a nuestro proyecto final! \n Este es el menú de opciones: \n 1- Agregar contacto. \n 2- Buscar contacto. \n 3- Eliminar contacto. \n 4- Ver contactos. \n 5- Editar contacto. \n 6- Eliminar todos los contactos. \n 0- Salir.")
    print("===================================================")

mostrar_menu()
opcion = int(input("¿Que acción desea realizar?"))

# POR SI EL USUARIO INGRESA UN NUMERO DISTINTO A LOS QUE ESTAN EN EL MENU DE OPCIONES
while opcion not in opciones:
    print("Esta opción no existe, ingrese una opción válida.")
    mostrar_menu()
    opcion= int(input("¿Qué acción desea realizar? \n")) 
    
# UN MENSAJITO PARA CUANDO EL USUARIO DESEE SALIR DEL PROGRAMA
while opcion != 0 :
    
    # Agregar contacto
    if opcion == 1:
        nombre= input ("Ingrese el nombre del contacto que desea agregar: ")
        telefono= input("Ingrese el número del contacto que desea agregar: ")
        telefono = telefono.replace("-", "")
        correo= input("Ingrese el correo electrónico del contacto que desea agregar: ")
        if correo== "":
            correo= "Sin correo electrónico."
        contacto= {"Nombre": nombre, "Teléfono": telefono, "Correo electrónico": correo}
        contactos.append(contacto)

        print(f"Contacto agregado de manera exitosa: \n Nombre: {nombre} \n Telefono: {telefono} \n Correo electronico: {correo}")
    mostrar_menu()
    opcion = int(input("¿Qué acción desea realizar? \n"))
print("===================================================")
print("¡Gracias por utilizar nuestra aplicación!")
print("Ha sido un placer ayudarte.")
print("¡Esperamos volver a verte pronto!")
print("===================================================")
       
