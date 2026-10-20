
#Este es el archivo principal del programa, el cual se encarga de la entrada y salida de datos. 

from calculo_totales import totales;
from calculo_maximo import maximo;
from calculo_minimo import minimo;

dias=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
botellas= [];


for dia in dias:
    cantidad= int(input(f'Ingrese la cantidad de botellas el {dia}: '))
    botellas.append(cantidad)
    
print ('Botellas por días:', botellas);

total_botellas = totales(botellas);
maximo_botellas = maximo(botellas);
minimo_botellas= minimo(botellas);

print('--------------------TOTALES Y ESTADISTICAS--------------------')
print(f'Total de botellas recicladas en la semana: {total_botellas}')
# print(f'Promedio diario de botellas recicladas: '{})
print(f'Día con mayor candidad de botellas recicladas: {maximo_botellas}')
# print(f'Día con menor candidad de botellas recicladas: '{})

#! reemplazar el 10 por las botellas que hay que reciclar realmente, el valor se encuentra en el calculo extra.
print(f'Esta semana se reciclaron {total_botellas} botellas.\n ¿Sabías que reciclando 10 botellas en la próxima semana \n pueden superar estos resultados en un 10%?\n ¡Cada pequeño cambio puede hacer de este mundo un lugar mejor!')