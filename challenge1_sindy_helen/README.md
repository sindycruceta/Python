# Documentación explicativa del contador ecológico

Esta documentación explica el funcionamiento del contador ecológico desarrollado por Helen Concepción y Sindy Cruceta para la iniciativa de reciclaje de la ciudad Verdesol. Esta iniciativa tiene el objetivo de reciclar la mayor cantidad posible de botellas plásticas al día para reducir el impacto ambiental de estos residuos en las fuentes de agua de la zona.

El programa permite registrar las botellas recicladas durante los siete días de la semana. A partir de estos datos, calcula el total semanal, el promedio diario y los días con mayor y menor cantidad de botellas recicladas. Estos resultados permiten conocer el progreso de la iniciativa y establecer una meta para la próxima semana.

El archivo principal gestiona la entrada y salida de datos. Contiene una lista con los días de la semana y otra que almacena las cantidades ingresadas. Utiliza un ciclo while para solicitar los datos al usuario y una estructura condicional if-else para identificar los valores negativos y guardar las cantidades válidas.

Dentro del archivo principal se importan las funciones de calculo_totales y bonus. Esta separación permite organizar el programa y mantener los cálculos en archivos distintos del registro y la presentación de los datos.

El archivo calculo_totales contiene las funciones calcular_totales y calcular_extremos. La primera recorre la lista de botellas con un ciclo for para sumar las cantidades y calcular el promedio diario. La segunda compara los valores registrados para identificar la mayor y menor cantidad de botellas, junto con los días correspondientes.

El archivo bonus contiene el cálculo de cuántas botellas se deben reciclar para aumentar el total actual en un 10 % durante la semana siguiente. También divide la nueva meta entre los siete días y utiliza math.ceil para redondear hacia arriba la cantidad diaria necesaria para alcanzarla.

Finalmente, el programa muestra las cantidades registradas por día, las estadísticas de la semana y la meta propuesta. Esta información ayuda a evaluar los resultados del reciclaje y motiva a los participantes a alcanzar nuevas metas de reciclaje y cuidado ambiental. 