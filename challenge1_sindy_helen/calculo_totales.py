
def calcular_totales (botellas):
    total=0
    for cantidad in botellas:
        total+= cantidad
    promedio= total /len(botellas)
    return total, promedio

def calcular_extremos(botellas, dias):
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