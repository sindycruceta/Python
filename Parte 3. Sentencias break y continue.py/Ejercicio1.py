#Escribe un programa que imprima todos los números del 1 al 20, pero use continue para saltar los números impares.
for i in range(1,21):
    if i%2==1:
        continue
    print(i)
    
