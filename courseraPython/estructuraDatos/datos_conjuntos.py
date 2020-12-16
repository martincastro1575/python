#elementos de un conjunto o contexto
#Un conjunto no genera elementos duplicados
frutas = {'manzana','naranja','manzana','pera','naranja','banana','kiwi'} #{'manzana','pera','naranja','banana','kiwi'}

'pera' in frutas #devuele True
'yerba' in frutas #devuele false

#conjunto vacio
set()

#otra forma de crear conjuntos
a = set('abracadabra') #{'a', 'b', 'c', 'd', 'r'} , elimina las letras repetidas
b = set('alakazam') #{'a', 'm', 'l', 'z', 'k'}

#operaciones de conjunto
a - b #{'d', 'r', 'b', 'c'}, letras en (a) pero no en (b)
a | b #{'a', 'b', 'c', 'd', 'm', 'l', 'r', 'z', 'k'}, letras en (a) o en (b) o en ambas
a & b #{'a'}, letras en (a) y en (b)
a ^ b #{'d', 'm', 'l', 'b', 'c', 'r', 'z', 'k'}, letras en (a) o en (b) pero no en ambas

#conjunto por comprension
a = {x for x in 'abracadabra' if x not in 'abc'}

#agregando elementos al conjunto
a.add('z')

#removiendo elementos al conjunto
a.remove('z')
