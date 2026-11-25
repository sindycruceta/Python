# Este programa recibe una lista de productos y devuelve el total a pagar por el usuario.
tienda = {
    "manzana": 20,
    "pan": 10,
    "leche":100,
    "queso": 200,
    "cafe": 150,
    "azucar": 65,
    "mantequilla": 50
}

print("Productos disponibles en la tienda:")
for prod, precio in tienda.items():
    print(f"- {prod}: ${precio}")
print("------------------------------")


cantidad_productos = int(input("¿Cuántos productos deseas agregar a tu lista de compras?: "))

total_pagar = 0
lista_compras = []

for i in range(cantidad_productos):
    producto_elegido = input(f"Ingrese el nombre del producto {i+1}: ").lower().strip()
    
    if producto_elegido in tienda:
        lista_compras.append(producto_elegido)
        total_pagar += tienda[producto_elegido]
    else:
        print(f"Lo sentimos, '{producto_elegido}' no está disponible.")

print("\n==============================")
print("RESUMEN DE TU COMPRA:")
for prod in lista_compras:
    print(f"- {prod}: ${tienda[prod]}")

print("------------------------------")
print(f"TOTAL A PAGAR: ${total_pagar}")
print("==============================")
