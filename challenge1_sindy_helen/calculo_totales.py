
#Esta función calcula el total de botellas ingresadas durante toda la semana y calcula el promedio. 
def calcular_totales (botellas): 
    total=0
    for cantidad in botellas:
        total+= cantidad
    promedio= total /len(botellas)
    return total, promedio

def calcular_extremos(botellas, dias): #Esta función calcula a partir de un ciclo for cuál es la mayor y menor cantidad comparando los valores de la lista en cada posición. 
    mayor = botellas [0]
    menor = botellas [0]
    dia_mayor = dias[0]
    dia_menor = dias[0]

    for i in range(len(botellas)):
        if botellas[i] > mayor:
            mayor = botellas[i]
            dia_mayor= dias [i]
        if botellas [i] < menor:
            menor= botellas [i]
            dia_menor= dias[i]
    return mayor, dia_mayor, menor, dia_menor