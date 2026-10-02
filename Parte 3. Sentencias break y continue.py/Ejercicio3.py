#Escribe un programa que imprima los números del 1 al 10. Usa continue para saltar los números pares y break para detener el ciclo cuando se llegue al número 9.
for i in range(1,11):
    if i%2==0:
       continue
    elif i==9:
       break
    print(i)
