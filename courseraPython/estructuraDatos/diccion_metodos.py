precios = {'manzana':3.5, 'banana':2.4,'kiwi':5.2,'pera':2.0}

#cantidad de elementos clave-valor
len(precios)

#Obtiene el valor para las claves indicadas, se puede indicar in valor default si no existe
precios.get('manzana')
precios.get('melon')
precios.get('melon', 0.00)

#Si existe devuelve el valor, sino lo crea con el valor default o si no se indica el default None
precios.setdefault('banana')
precios.setdefault('sandia', 6.3)

#actualizando elementos en un diccionario, si el elemento no existe lo agrega al diccionario
precios.update({'banana':3.0, 'durazno':4.2})
precios.update([('durazno',4.1)])

#devuelve una vista con las claves del diccionario
precios.keys()

#devuelve una vista con los valores del diccionario
precios.values()

#devuelve una vista con los items del diccionario
precios.items()

#saca el elemento de la clave indicada devolviendo el valor de la clave indicada, 
# si no existe se puede indicar un valor por default
precios.pop('manzana')
precios.pop('melon', 0.00)
precios.pop('guayaba')#como no existe devuelve un KeyError

#Saca un elemento siguiendo el orden: LIFO
precios.popitem()

#Crea una copia supercial del diccionario
copia_precios = precios.copy()

#borra todos los elementos del diccionario
precios.clear()
