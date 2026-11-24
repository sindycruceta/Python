# = Proyecto final de Sindy Cruceta y Helen Concepcion: Gestor de contactos.
# & Lista de opciones válidas del menú (0 es para salir)
opciones= [1,2,3,4,5,6,0]
#& Lista vacía donde se irán guardando todos los contactos
contactos= []
#? Función para mostrar el menú de opciones en pantalla
def mostrar_menu():
    print("===================================================")
    print("Te damos la bienvenida a nuestro proyecto final! \n Este es el menú de opciones: \n 1- Agregar contacto. \n 2- Buscar contacto. \n 3- Eliminar contacto. \n 4- Ver contactos. \n 5- Editar contacto. \n 6- Eliminar todos los contactos. \n 0- Salir.")
    print("===================================================")

mostrar_menu()
opcion = int(input("¿Que acción desea realizar?"))

#? POR SI EL USUARIO INGRESA UN NUMERO DISTINTO A LOS QUE ESTAN EN EL MENU DE OPCIONES
while opcion not in opciones:
    print("Esta opción no existe, ingrese una opción válida.")
    mostrar_menu()
    opcion= int(input("¿Qué acción desea realizar? \n")) 
    
#? Ciclo principal. El programa se repite hasta que el usuario elija 0 para salir
while opcion != 0 :
    
     # * AGREGAR CONTACTO:
    if opcion == 1:
        nombre= input ("Ingrese el nombre del contacto que desea agregar: ")
        telefono= input("Ingrese el número del contacto que desea agregar: ")
        telefono = telefono.replace("-", "")
        correo= input("Ingrese el correo electrónico del contacto que desea agregar, o presione Enter para omitirlo: ")
        if correo== "":
            correo= "Sin correo electrónico."
        contacto= {"Nombre": nombre, "Teléfono": telefono, "Correo electrónico": correo}
        contactos.append(contacto)

        print(f"Contacto agregado de manera exitosa: \n Nombre: {nombre} \n Telefono: {telefono} \n Correo electronico: {correo}")
        
        # * BUSCAR CONTACTO:
    if opcion == 2:
        buscar= input("Ingrese el nombre del contacto que desee buscar: ").lower()
        cantidad = 0
        for contacto in contactos:
            if buscar== contacto["Nombre"].lower():
                print("¡Listo! Su contacto fue encontrado con éxito. Los datos del mismo son: ")
                print("Nombre: ", contacto["Nombre"])
                print("Teléfono:", contacto["Teléfono"])
                print("Correo:", contacto["Correo electrónico"])
                cantidad = cantidad+1
        if cantidad == 0:
            print("No se encontró ningun contacto agregado con ese nombre.")
            
        # * ELIMINAR CONTACTO:
    if opcion == 3:
        eliminar= input("Ingrese el nombre del contacto que desee eliminar: ").lower()
        eliminados = 0
        for contacto in contactos:
            if eliminar == contacto["Nombre"].lower():
                contactos.remove(contacto)
                eliminados= eliminados + 1
        if eliminados == 0:
            print("No se encontró ningún contacto con ese nombre.")
        else:
            print("El contacto fue eliminado con éxito.")
        
    mostrar_menu()
    opcion = int(input("¿Qué acción desea realizar? \n"))
    
    #? MENSAJE DE AGRADECIMIENTO POR USAR EL PROGRAMA, SE MOSTRARÁ CUANDO EL USUARIO DESEE SALIR DEL PROGRAMA

print("===================================================")
print("¡Gracias por utilizar nuestra aplicación!")
print("Ha sido un placer ayudarte.")
print("¡Esperamos volver a verte pronto!")
print("===================================================")
       
