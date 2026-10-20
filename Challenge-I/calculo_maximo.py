#Esta funcion compara el valor de la lista botellas en las 7 posiciones para determinar cuál es el número mayor

def maximo(botellas):
    if botellas[0] > botellas[1]:
        return 0;
    elif botellas[1] > botellas[2]:
        return 1;
    elif botellas[2] > botellas[3]:
        return 2;
    elif botellas[3] > botellas[4]:
        return 3;
    elif botellas[4] > botellas[5]:
        return 4;
    elif botellas[5] > botellas[6]:
        return 5;
    else: return 6;
print(f'El máximo de botellas es: {maximo}');