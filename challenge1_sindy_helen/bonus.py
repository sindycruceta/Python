#Esta función calcula cuántas botellas se deben reciclar para superar la cantidad actual en un 10%.

import math
def calcular_meta_semana_proxima(total_actual):
    meta_nueva = total_actual * 1.10
    por_dia = math.ceil(meta_nueva/ 7) #Utilizamos ceil para manejar decimales, redondeando al entero mayor más próximo al número original. 
    return meta_nueva, por_dia
   