precios = {'manzana':3.5, 'banana':2.4,'kiwi':5.2,'pera':2.0}

#vistas de diccionarios
claves = precios.keys()
valores = precios.values()
items = precios.items()

#Iteraccion de diccionarios
for fruta, precio in precios.items():
    print(f'Precio de {fruta} : {precio} $')