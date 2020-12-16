#lista de cuadrados
cuadrados=[]

for x in range(10):
    cuadrados.append(x**2)

#lista por comprension
cuadrados_2 = [x ** 2 for x in range(10)]

#Cuadrados utilizando la funcion map
cuadrados_3 = list(map(lambda x: x ** 2, range(10)))
aux_ficha
#Lista por comprension con numeros positivos
a_list = [-4,-2,0,1,2]
positivos = [x for x in a_list if x>=0]

#Lista de numeros positivos usando la funcion filter
positivos_2 = list(filter(lambda x: x>0 , a_list))

#Lista de pares de numero y su cuadrado
[(x,x ** 2) for x in range(6)]

#Lista de pares combinados
pares = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

