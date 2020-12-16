#maneras de crear diccionarios
precios = {'manzana':3.5, 'banana':2.4,'kiwi':5.2,'pera':2.0}
precios = dict(manzana=3.5, banana=2.4, kiwi=5.2, pera=2.0)
precios = dict([('manzana',3.5), ('banana',2.4),('kiwi',5.2),('pera',2.0)])

#acceso a los elementos por claves
precios['manzana'] #3.5
precios['kiwi'] #5.2
precios['pera'] #2.0
precios['tamarindo'] #KeyError

#agregando un elemento clave-valor
precios['melon'] = 3.93

#actualizando un elemento clave-valor
precios['manzana'] = 2.95

#borrando un elemento clave-valor
del precios['kiwi']

#pertenencia o verificar si una clave se encuentra en un diccionario
'banana' in precios #True
'tamarindo' in precios #False