
#!VERSION EDITADA

# = Proyecto final de Sindy Cruceta y Helen Concepcion: Gestor de contactos.
# & Lista de opciones válidas del menú (0 es para salir)
opciones_menu= [1,2,3,4,5,6,0]
opciones_eliminar= [0,1]
#& Listas vacías donde se irán guardando todos los contactos
nombres = []
telefonos = []
correos = []

print("Te damos la bienvenida a nuestro proyecto final!\n")

#? Función para mostrar el menú de opciones en pantalla
def mostrar_menu():
    print("===================================================")
    print("Este es el menú de opciones: \n 1- Agregar contacto. \n 2- Buscar contacto. \n 3- Eliminar contacto. \n 4- Ver contactos. \n 5- Editar contacto. \n 6- Eliminar todos los contactos. \n 0- Salir.")
    print("===================================================")

mostrar_menu()
opcion = int(input("¿Que acción desea realizar?"))

#? POR SI EL USUARIO INGRESA UN NUMERO DISTINTO A LOS QUE ESTAN EN EL MENU DE OPCIONES
while opcion not in opciones_menu:
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
        nombres.append(nombre)
        telefonos.append(telefono)
        correos.append(correo)

        print(f"Contacto agregado de manera exitosa: \n Nombre: {nombre} \n Telefono: {telefono} \n Correo electronico: {correo}\n\n")
        
        mostrar_menu()
        opcion = int(input("¿Que acción desea realizar?"))
        
        # * BUSCAR CONTACTO:
    elif opcion == 2:
        buscar= input("Ingrese el nombre del contacto que desee buscar: ").lower()
        cantidad = 0
        for i in range(len(nombres)):
            if buscar == nombres[i].lower():
                print("¡Listo! Su contacto fue encontrado con éxito. Los datos del mismo son: ")
                print("Nombre: ", nombres[i])
                print("Teléfono:", telefonos[i])
                print("Correo:", correos[i])
                cantidad = cantidad+1
        if cantidad == 0:
            print("No se encontró ningun contacto agregado con ese nombre.")
            
        # * ELIMINAR CONTACTO:
    elif opcion == 3:
        eliminar= input("Ingrese el nombre del contacto que desee eliminar: ").lower()
        eliminados = 0
        for i in range (len(nombres)):
            if eliminar == nombres[i].lower():
                nombres.remove(nombres)
                eliminados= eliminados + 1
        if eliminados == 0:
            print("No se encontró ningún contacto con ese nombre.")
        else:
            print("El contacto fue eliminado con éxito.")
            
        #*  VER CONTACTOS
        
    elif opcion == 4:
        print("Contactos existentes:\n")

        for nombres,telefonos,correos in zip(nombres,telefonos,correos):
            print(f"{nombre}, {telefono}, {correo}")
        mostrar_menu()
        opcion = int(input("¿Que acción desea realizar?"))
        
    
    #*  EDITAR CONTACTO
    elif opcion == 5:
        contacto_editar= int(input("Ingrese el nombre del contacto que desea editar..."))
        for nombre in nombres:
            if nombre["nombre"]== contacto_editar:
                print("Este es el contacto a editar")
        
    #*  ELIMINAR TODOS LOS CONTACTOS
    elif opcion == 6:
        eliminar_todos= int(input("¿Está seguro de que desea eliminar todos los contactos? escriba 0 para cancelar, 1 para confirmar"))
        while eliminar_todos not in opciones_eliminar:
            print("Las opciones validas son 0 y 1")
        if eliminar_todos== 1:
            nombres.clear()
            telefonos.clear()
            correos.clear()
            print("Se han eliminado todos los contactos")
        else: 
                mostrar_menu()
    
    #? MENSAJE DE AGRADECIMIENTO POR USAR EL PROGRAMA, SE MOSTRARÁ CUANDO EL USUARIO DESEE SALIR DEL PROGRAMA

print("===================================================")
print("¡Gracias por utilizar nuestra aplicación!")
print("Ha sido un placer ayudarte.")
print("¡Esperamos volver a verte pronto!")
print("===================================================")
       
