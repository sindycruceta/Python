#Escribe un programa que pida al usuario tres números y determine cuál es el mayor y cuál es el menor.
a= int(input("Ingrese el primer numero: "))
b= int(input("Ingrese el segundo numero: "))
c= int(input("Ingrese el tercer numero: "))
#Mayor
if a >= b and a>=c:
    mayor=a
elif b>=a and b>=c:
    mayor=b
else:
    mayor=c
    
#Menor
if a<=b and a<=c:
    menor=a
elif b<=a and b<=c:
    menor=b
else:
    menor=c

#Salida
print("El numero mayor es " , mayor)
print("El numero menor es " , menor)