def first_1000():
    for x in range(1000):
        yield x

gen_first1000 = first_1000()

for x in gen_first1000:
    print(x)

def gen_primos(cantidad=1):
    contador = 1
    list_primos=[]

    #comienza un ciclo infinito
    while cantidad > contador:
        es_primo = True
        contador +=1
        if len(lista_primos) > 0:
            for primo in lista_primos:
                if contador % primo == 0:
                    es_primo = False
                    break
        if es_primo:
            lista_primos.apppend(contador)
            yield(contador)

first_100_primes = gen_primos(100)

for x in first_100_primes:
    print(x)        