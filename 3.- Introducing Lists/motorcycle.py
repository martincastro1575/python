motorcycles = ['honda','yamaha','suzuki']

print('Lista original:', motorcycles)

#change the value of the first item
motorcycles[0] = 'ducati'
print('Modificando valor del primer elemento:', motorcycles)

#Appending elements to the end of the list
motorcycles.append('honda')
print('Agregando un elemento al final de la lista:', motorcycles)

#Appendig elements to empty list
motorcycles_empty = []
motorcycles_empty.append('bellini')
motorcycles_empty.append('vespa')
motorcycles_empty.append('bajaj')
motorcycles_empty.append('beta')
print('Agregando elementos a una lista vacia: ',motorcycles_empty)

#Inserting elements into a list
motorcycles_empty.insert(0,'ducati')
print('Insetando un elemento a la lista: ', motorcycles_empty)

#Removing an item using the del stament
del motorcycles_empty[1]
print('Removiendo el segundo elemento de llista: ', motorcycles_empty)

#Removing an item using the pop() method
motorcycles = ['honda','yamaha','suzuki']
print('Lista antes de usar el metodo pop() ', motorcycles)
popped_motorcycles = motorcycles.pop()
print('Lista depues de usar el metodo pop() ', motorcycles)
print('lista con el meotodo pop(): ' , popped_motorcycles)

motorcycles = ['benelli','yamaha','suzuki','ducati']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}. ")

#Popping item from any position in a list
first_owned = motorcycles.pop(0)
print(f"The first motorcicle I owned was a {first_owned.title()}")
print("Despues del pop ",motorcycles)

#Removing an item by value
motorcycles = ['benelli','yamaha','suzuki','ducati']
motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me. ")
