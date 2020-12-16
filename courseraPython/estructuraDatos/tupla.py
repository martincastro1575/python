tupla = (1, 2.5, 'Hola')

tupla[0] # 1
tupla[1] # 2.5
tupla[2] # 'Hola'

tupla[:2] #(1, 2.5)

#tupla vacia
tupla_vacia_1 = ()
tupla_vacia_2 = tuple()

#tupla de un elemento
tupla_2 = (5, ) #Esto es una tupla, prestar atencion a la coma despues del 5
numero = (5) #Esto es un numeri

#longitud de la tupla
len(tupla)

tupla[2] = 3 #Las tuplas son inmutables, esto da un error del tipo TypeError