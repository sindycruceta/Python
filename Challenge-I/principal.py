
#Este es el archivo principal del programa, el cual se encarga de la entrada y salida de datos. 
import math
from calculo_totales import calcular_totales, calcular_extremos
from bonus import calcular_meta_semana_proxima;

dias=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
botellas= [];

for dia in dias:
    cantidad= int(input(f'Ingresa la cantidad de botellas recicladas el {dia}: '))
    if cantidad < 0:
        print('Cantidad inválida, ingresa un número positivo.')
        break;
    else:
        botellas.append(cantidad)

        total, promedio= calcular_totales(botellas)
        mayor, dia_mayor, menor, dia_menor= calcular_extremos(botellas, dias)    
        print ('Botellas por días:', botellas)


        print('--------------------TOTALES Y ESTADISTICAS--------------------')
        print(f'Total de botellas recicladas en la semana: {total}')
        print(f"Promedio diario de botellas recicladas: {promedio:.2f}")
        print(f'Día con mayor candidad de botellas recicladas: {dia_mayor} ({mayor} botellas)')
        print(f"Día con menor candidad de botellas recicladas: {dia_menor} ({menor} botellas)")

        meta_nueva, por_dia = calcular_meta_semana_proxima(total)

        print("--------------------META PARA LA PROXIMA SEMANA---------------")
        print(f"Meta actual (total de esta semana): {total}")
        print(f"Meta para superarla en 10%: {meta_nueva:.1f} botellas")
        print(f"Deben reciclar al menos {por_dia} botellas por dia")
        #!RECUERDA REEMPLAZAR EL 10 POR LA META NUEVA
        print(f'Esta semana se reciclaron {total} botellas.\n ¿Sabías que reciclando 10 botellas en la próxima semana \n pueden superar estos resultados en un 10%?\n ¡Cada pequeño cambio puede hacer de este mundo un lugar mejor!')
