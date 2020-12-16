a_list = [3, 7.5, 'Hola', 7j + 5, [1, 2]]

#Acceso mediante sus indices
a_list[0] #3
a_list[2] #'Hola'
a_list[-1] #[1, 2]

#Cortando lista o haciendo una sublista
a_list[1:] # [7.5, 'Hola', 7j + 5, [1, 2]]
a_list[1:2] # [7.5]
a_list[1:3] # [7.5, 'Hola']
a_list[:2] # [3, 7.5]
a_list[:] # [3, 7.5, 'Hola', 7j + 5, [1, 2]]

#Algunas funciones

#Devuelve la cantidad de elementos de una lista
len(a_list) #5

#agrega un elemento al final de la lista
a_list.append(3) #[3, 7.5, 'Hola', 7j + 5, [1, 2], 3]

#Extiende la lista con otros elemento de una lista y los coloca al final de la lista
a_list.extend(['u',4,'L']) #[3, 7.5, 'Hola', (5+7j), [1, 2], 3, 'u', 4, 'L']

#Insertando un elemento en una lista
a_list.insert(3,'New Element') #[3, 7.5, 'Hola', 'New Element', (5+7j), [1, 2], 3, 'u', 4, 'L']

#Si coloco un indice fuera de rango, se agrega al final de la lista
a_list.insert(13,'Fuera de Rango') #[3, 7.5, 'Hola', 'New Element', (5+7j), [1, 2], 3, 'u', 4, 'L', 'Fuera de Rango']

#Inserta elemento en la penultima posicion
a_list.insert(-1,'Hacia atras') #[3, 7.5, 'Hola', 'New Element', (5+7j), [1, 2], 3, 'u', 4, 'L', 'Hacia atras', 'Fuera de Rango']

#Cuenta cuantos elementos coinciden con el argumento
a_list.count(3) #2

#Elimina el primer elemento de la lista que coincidada con el argumento pasado como parametro
a_list.remove(3) #elimina el primer 3 que consiga

#Para hacer una copia superficial de la lista
a_list_copy = a_list.copy()

a_list.pop() #Quita y devuelve el ultimo elemento de la lista

a_list.pop(3) #Quita y devuelve el elemento indicado como argumento

#Borrando todos los elementos de la lista
a_list.clear() #[]




