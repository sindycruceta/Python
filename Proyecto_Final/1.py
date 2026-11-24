# Proyecto final de Sindy Cruceta y Helen Concepcion: Gestor de contactos.
opciones= [1,2,3,4,5,6,0]
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
else:
    if opcion==0:
        print("===================================================")
        print("¡Gracias por utilizar nuestra aplicación!")
        print("Ha sido un placer ayudarte.")
        print("¡Esperamos volver a verte pronto!")
        print("===================================================")
        
