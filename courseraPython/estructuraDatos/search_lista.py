a_lista = [1,2,3,4,5]

#busqueda por indice, devuelve la posicion o indice del elemento pasado en el argumento
a_lista.index(3) #2
a_lista.index(5) #4

#si el elemento no esta en la lista devuelve un error del tipo ValueError
a_lista.index(0) #ValueError: 0 is not in list

#Buscando indicando una sublista, en el primer argumento se indica el elemento a buscar 
# y en el segundo argumento se indica a partir de que indice se da inicio la busqueda.
a_lista.index(2,0) #1
a_lista.index(4,2) #3

#Especificando, elemento a buscar, indice de inicio de busqueda, indice final de busqueda
a_lista.index(2,0,3) #1

#Si el elemento no se encuentra dentro de los indices de busqueda devuelve un error de tipo ValueError
a_lista.index(2,2,3) #ValueError: 2 is not in list
