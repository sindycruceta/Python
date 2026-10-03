#Este algoritmo recibe una calificación y le asigna una letra.

nota = float(input("Ingrese la calificación: "));

if nota >=90 and nota <=100:
    print("La calificación es A");
elif nota >=80 and nota <90:
    print("La calificación es B");
elif nota >=70 and nota <80:
    print("La calificación es C");
elif nota >=60 and nota <70:
    print("La calificación es D");  
else:
    print("La calificación es F");
    