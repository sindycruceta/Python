
#Este es el archivo principal del programa, el cual se encarga de la entrada y salida de datos. 
import math
from calculo_totales import calcular_totales, calcular_extremos
from bonus import meta_nueva;

dias=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
botellas= [];


for dia in dias:
    cantidad= int(input(f'Ingrese la cantidad de botellas el {dia}: '))
    botellas.append(cantidad)

total, promedio= calcular_totales(botellas)
mayor, dia_mayor, menor, dia_menor= calcular_extremos(botellas, dias)    
print ('Botellas por días:', botellas)


print('--------------------TOTALES Y ESTADISTICAS--------------------')
print(f'Total de botellas recicladas en la semana: {total}')
print(f"Promedio diario de botellas recicladas: {promedio:.2f}")
print(f'Día con mayor candidad de botellas recicladas: {dia_mayor} ({mayor} botellas')
print(f"Día con menor candidad de botellas recicladas: {dia_menor} ({menor} botellas ")

# reemplazar el 10 por las botellas que hay que reciclar realmente, el valor se encuentra en el calculo extra(bonus).


print("--------------------META PARA LA PROXIMA SEMANA---------------")
print(f"Meta actual (total de esta semana): {total}")
print(f"Meta para superarla en 10%: {meta_nueva:.1f} botellas")
print(f'Esta semana se reciclaron {total} botellas.\n ¿Sabías que reciclando 10 botellas en la próxima semana \n pueden superar estos resultados en un 10%?\n ¡Cada pequeño cambio puede hacer de este mundo un lugar mejor!')

