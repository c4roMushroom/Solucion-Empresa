cant = int(input("ingrese la cantidad de ventas del día: "))

listav = {}

for x in range(0,cant): 
    producto = input("ingrese el producto vendido: ")
    venta = int(input("ingrese las unidades vendidas: "))

    if producto not in listav:
        listav[producto] = [venta]
    else:
        listav[producto].append(venta)
    
for producto, ventas in listav.items():
    ventasT = sum(ventas)
    print(f"Total de ventas de {producto}: {ventasT}")

