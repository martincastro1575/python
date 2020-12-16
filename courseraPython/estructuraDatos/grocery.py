precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75, 'ciruela': 2.45, 'durazno': 4.55, 'melon': 7.35, 'sandia': 9.70, 'anana': 11.25}

def subtotal(kilo, precio):
    sub = kilo * precio
    
    return sub


suma=0
for fruta, precio in precios.items():
    kilo = input(f"Ingre los kilos de {fruta}: \n")
    val= subtotal(float(kilo), precio)
    print(f'El costo de {kilo} kilos de {fruta} es: {val}')
    suma += val
    #print (f'El valor de la {fruta} es {precio}$')
print(f"El total del tickect es: {suma}")