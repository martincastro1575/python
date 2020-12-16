import time
import os
def tablero():
    print('\n\t\t|',matriz[0][0],'|',matriz[0][1],'|',matriz[0][2],'|\n')
    print('\t\t|',matriz[1][0],'|',matriz[1][1],'|',matriz[1][2],'|\n')
    print('\t\t|',matriz[2][0],'|',matriz[2][1],'|',matriz[2][2],'|\n')

def evaluar():
    if matriz[0][0]==matriz[0][1] and matriz[0][1]==matriz[0][2]:
        print('Ganó',jugador,'!!!')
        return True
    elif matriz[1][0]==matriz[1][1] and matriz[1][1]==matriz[1][2]:
        print('Ganó',jugador,'!!!')
        return True
    elif matriz[2][0]==matriz[2][1] and matriz[2][1]==matriz[2][2]:
        print('Ganó',jugador,'!!!')
        return True
    elif matriz[0][0]==matriz[1][0] and matriz[1][0]==matriz[2][0]:
        print('Ganó',jugador,'!!!')
        return True
    elif matriz[0][1]==matriz[1][1] and matriz[1][1]==matriz[2][1]:
        print('Ganó',jugador,'!!!')
        return True
    elif matriz[0][2]==matriz[1][2] and matriz[1][2]==matriz[2][2]:
        print('Ganó',jugador,'!!!')
        return True
    elif matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2]:
        print('Ganó',jugador,'!!!')
        return True
    elif matriz[0][2]==matriz[1][1] and matriz[1][1]==matriz[2][0]:
        print('Ganó',jugador,'!!!')
        return True

def seleccion():
    while True:
        try:
            x=int(input('Selecciona una casilla '+jugador+'\n'))
            while x>9 or x<1:
                print("No existe la celda seleccionada")
                x=int(input('Selecciona una casilla '+jugador+'\n'))        
            return x
        except ValueError:
            print("No seleccionaste un número, vuelve a intentar\n")

def marca(x):
    if x==1:
        if matriz[0][0]=='X' or matriz[0][0]=='O':
            print("Celda ocupada, vuelve a seleccionar\n")
            return False
        else:
            matriz[0][0]=jugador
            return True
    elif x==2:
        if matriz[0][1]=='X' or matriz[0][1]=='O':
            print("Celda ocupada, vuelve a seleccionar\n")
            return False
        else:
            matriz[0][1]=jugador
            return True
    elif x==3:
        if matriz[0][2]=='X' or matriz[0][2]=='O':
            print("Celda ocupada, vuelve a seleccionar\n")
            return False
        else:
            matriz[0][2]=jugador
            return True
    elif x==4:
        if matriz[1][0]=='X' or matriz[1][0]=='O':
            print("Celda ocupada, vuelve a seleccionar\n")
            return False
        else:
            matriz[1][0]=jugador
            return True
    elif x==5:
        if matriz[1][1]=='X' or matriz[1][1]=='O':
            print("Celda ocupada, vuelve a seleccionar\n")
            return False
        else:
            matriz[1][1]=jugador
            return True
    elif x==6:
        if matriz[1][2]=='X' or matriz[1][2]=='O':
            print("Celda ocupada, vuelve a seleccionar\n")
            return False
        else:
            matriz[1][2]=jugador
            return True
    elif x==7:
        if matriz[2][0]=='X' or matriz[2][0]=='O':
            print("Celda ocupada, vuelve a seleccionar\n")
            return False
        else:
            matriz[2][0]=jugador
            return True
    elif x==8:
        if matriz[2][1]=='X' or matriz[2][1]=='O':
            print("Celda ocupada, vuelve a seleccionar\n")
            return False
        else:
            matriz[2][1]=jugador
            return True
    elif x==9:
        if matriz[2][2]=='X' or matriz[2][2]=='O':
            print("Celda ocupada, vuelve a seleccionar\n")
            return False
        else:
            matriz[2][2]=jugador
            return True
def tiro():
    for contador in range(1,10):
        yield contador

matriz=[[1,2,3],[4,5,6],[7,8,9]]
os.system('cls')
print('''\t\tJuego TA TE TI
\tEmpiezan las X y continuan los O''')
for contador in range(1,10):
    tablero()
    if contador%2==1:
        jugador='X'
    else:
        jugador='O'
    while marca(seleccion())==False:
        os.system('cls')
        tablero()
        marca(seleccion())
    if evaluar() ==True:
        os.system('cls')
        tablero()
        evaluar()
        break
    os.system('cls')
if contador==9:
    os.system('cls')
    tablero()
    print('Empate!!!')
time.sleep(5)