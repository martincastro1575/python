nombre = 'Martin'

lista = list(nombre)

#La indexacion funciona para el string y la lista
nombre[0]
lista[0]

#El slicing funciona para string y lista
nombre[:4]
lista[:4]

#La funcion len funciona para ambas
len(nombre)
len(lista)

#El in funciona de igual forma
'r' in nombre
'r' in lista

#El not funciona de igual forma
'x' not in nombre
'x' not in lista

#Tambien podemos recorrer los string con for
for letra in nombre:
    print(letra)


#Los string son inmutables pero podemos construir nuevos string a partir de string anteriores
new_name = nombre[:3] + 'i' + nombre[5:]# Marin