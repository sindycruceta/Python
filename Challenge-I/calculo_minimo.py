#Este algoritmo calcula el día maximo y mínimo de botellas recicladas:
from principal import dias;
from principal import botellas;
from calculo_totales import mayor;
from calculo_totales import menor;

for i in range(len(botellas)):
    if botellas[i] > mayor:
        mayor = botellas [i]
        dia_mayor = dias[i]
    if botellas [i] < menor:
        menor = botellas [i]
        dia_menor = dias [i]

    