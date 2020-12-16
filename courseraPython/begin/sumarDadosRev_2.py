from random import choice

def tirar_dado():
    """ Simula el tiro de un dado e imprime el resultado """
    resultado = choice([1,2,3,4,5,6])
    print("Resultado de tirar dado: ", resultado)
    return resultado

def calcular_suma_dados():
    """ Tira dos veces un dado y los suma """
    primerTiro, segundoTiro = tirar_dado(), tirar_dado()
    print("Resultado de la suma: ", primerTiro + segundoTiro, end='\n\n')

def tirar_otra_vez():
    """ Devuelve un booleano según lo que ingrese el usuario """
    if(input("Si desea tirar dados nuevamente, presione s\n") == "s"):
        return True
    else:
        return False

calcular_suma_dados()

while(tirar_otra_vez()):    
    """ Mientras que el usuario ingrese s se seguirá sumando el resultado de tirar dos veces un dado """
    calcular_suma_dados()