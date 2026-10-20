import math
def calcular_meta_semana_proxima(total_actual):
    meta_nueva = total_actual * 1.10
    por_dia = math.ceil(meta_nueva/ 7)
    return meta_nueva, por_dia
   