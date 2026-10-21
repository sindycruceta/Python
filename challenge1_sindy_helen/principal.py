
'''Este es el archivo principal del programa, el cual se encarga de la entrada y salida de datos. 
Nombres: Helen Concepción, Sindy Cruceta.
Matrículas: 2026-0341 , 2024-1034.
'''

#Estas importaciones corresponden a los archivos que contienen los cálculos a utilizar para procesar los datos.
import math
from calculo_totales import calcular_totales, calcular_extremos
from bonus import calcular_meta_semana_proxima;

dias=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"] #Listas con los días de la semana y lista vacía para almacenar las botellas por día.
botellas= [];
i=0; #Variable de control

#Este ciclo utiliza la variable i para controlar las vueltas. 
while i < len(dias): #si es menor a la longitud del arreglo de días, le pide al usuario que ingrese la cantidad de botellas.
    dia= dias[i];
    cantidad= int(input(f'Ingresa la cantidad de botellas recicladas el {dia}: '))
    if cantidad < 0:
            print('Ingrese una cantidad positiva.') #Aquí validamos que se ingresen siempre cantidades positivas.
            i = i-1; #Restamos 1 a la variable de control para pedir el valor del último día ingresado. 
    else:
        i = i +1;
        botellas.append(cantidad) #Si la cantidad es válida, agregamos un elemento a la lista de botellas.

total, promedio= calcular_totales(botellas)
mayor, dia_mayor, menor, dia_menor= calcular_extremos(botellas, dias)

#Imprimimos en consola los resultados con un formato legible para el usuario.

print('\n')
print('--------------------BOTELLAS POR DIAS--------------------')

for dia, botellas in zip(dias,botellas):
    print(f"{dia}: {botellas}")
    
print('\n')
print('--------------------TOTALES Y ESTADISTICAS--------------------')
print(f'Total de botellas recicladas en la semana: {total}')
print(f"Promedio diario de botellas recicladas: {round(promedio)}")
print(f'Día con mayor candidad de botellas recicladas: {dia_mayor} ({mayor} botellas)')
print(f"Día con menor candidad de botellas recicladas: {dia_menor} ({menor} botellas)")

meta_nueva, por_dia = calcular_meta_semana_proxima(total)
print('\n')
print("--------------------META PARA LA PROXIMA SEMANA---------------")
print(f"Meta actual (total de esta semana): {total}")
print(f'Esta semana se reciclaron {total} botellas.\n ¿Sabías que reciclando {round(meta_nueva)} botellas en la próxima semana \n pueden superar estos resultados en un 10%?')
print(f"Deben reciclar al menos {por_dia} botellas por día para alcanzar esta meta.")
print("¡Cada pequeño cambio puede hacer de este mundo un lugar mejor!")
