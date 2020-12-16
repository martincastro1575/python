import random


def lanzar_dados(val=list(range(1,7)),bol=True):
    
    while bol == True:
        tirada =random.choices(val,k=2)
        suma = sum(tirada)
        print(f"\tDado_A: {tirada[0]} - Dado_B: {tirada[1]}",f"\n\tSuma: {suma}")
        
        resp = input("¿Queres probar suerte de nuevo?:\n")

        if not resp in ('s','S','si','Si','SI'):
            bol = False
    return

lanzar_dados()

