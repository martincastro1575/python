a_list = [3,1,2,9,5,4,7,8,6]

#Ordena lo elementos permanentemente
a_list.sort() #Ordena de menor a mayor
a_list.sort(reverse=True) #Ordena de mayor a menor

#con el parametro key, permite ordenar la lista por medio de una funcion
a_list = [(1,9),(1,3),(1,4),(1,2)]
a_list.sort(key=lambda x: x[1]) #(1, 2), (1, 3), (1, 4), (1, 9)]

#orden de atras a delante y sivuelvo aplicar el reverse Revierte la ordenacion permanente 
a_list_reverse()

#Ordena los elementos y crea una lista nueva
sorted(a_list)
sorted(a_list, reverse=True)

#con el parametro key, permite ordenar la lista por medio de una funcion
a_list = [(1,9),(1,3),(1,4),(1,2)]
a_list.sort(key=lambda x: x[1]) #(1, 2), (1, 3), (1, 4), (1, 9)]


