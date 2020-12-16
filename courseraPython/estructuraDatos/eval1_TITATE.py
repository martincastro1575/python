def dib_tablero(tablero):
    for i in range(0,7,3):
        print(tablero[i]+'|'+tablero[i+1]+'|'+tablero[i+2])

print('Bienvenido al juego TA-TE-TI')
print('')
print('Este es el tablero y sus posiciones:')
print('1|2|3')
print('4|5|6')
print('7|8|9')
print('inicia X')
tablero=[' ']*9
juegofinal=Falsedef dib_tablero(tablero):
    for i in range(0,7,3):
        print(tablero[i]+'|'+tablero[i+1]+'|'+tablero[i+2])

print('Bienvenido al juego TA-TE-TI')
print('')
print('Este es el tablero y sus posiciones:')
print('1|2|3')
print('4|5|6')
print('7|8|9')
print('inicia X')
tablero=[' ']*9
juegofinal=False
tx=True
jugar_otravez=True
l=input('Â¿Quieres jugar?: S/N: ').upper()
if l=='S':
    while not juegofinal:
        juego_posible=False
        while not juego_posible:
            try:
                posicion=int(input('Ingrese la posiciÃ³n (1-9)=  '))
                if tablero[posicion-1]==' ':
                    juego_posible=True
                else:
                    print('PosiciÃ³n ocupada')
            except:
                print('Ese movimiento no es valido')
        tablero[posicion-1]='X' if tx else 'O'
        dib_tablero(tablero)
        if (tablero[0]==tablero[1]==tablero[2] and tablero[0]!=' ' or
            tablero[3]==tablero[4]==tablero[5] and tablero[3]!=' ' or
            tablero[6]==tablero[7]==tablero[8] and tablero[6]!=' ' or
            tablero[0]==tablero[3]==tablero[6] and tablero[0]!=' ' or
            tablero[1]==tablero[4]==tablero[7] and tablero[1]!=' ' or
            tablero[2]==tablero[5]==tablero[8] and tablero[2]!=' ' or
            tablero[0]==tablero[4]==tablero[8] and tablero[0]!=' ' or
            tablero[2]==tablero[4]==tablero[6] and tablero[2]!=' '):
            print('El ganador es:  '+'X' if tx else 'El ganador es:  '+'O')
            juegofinal=True
        if ' ' not in tablero:
            print('Es un empate')
            juegofinal=True
        tx=not tx
        
   
else:
    print('Hasta la proxima')
tx=True
jugar_otravez=True
l=input('Â¿Quieres jugar?: S/N: ').upper()
if l=='S':
    while not juegofinal:
        juego_posible=False
        while not juego_posible:
            try:
                posicion=int(input('Ingrese la posiciÃ³n (1-9)=  '))
                if tablero[posicion-1]==' ':
                    juego_posible=True
                else:
                    print('PosiciÃ³n ocupada')
            except:
                print('Ese movimiento no es valido')
        tablero[posicion-1]='X' if tx else 'O'
        dib_tablero(tablero)
        if (tablero[0]==tablero[1]==tablero[2] and tablero[0]!=' ' or
            tablero[3]==tablero[4]==tablero[5] and tablero[3]!=' ' or
            tablero[6]==tablero[7]==tablero[8] and tablero[6]!=' ' or
            tablero[0]==tablero[3]==tablero[6] and tablero[0]!=' ' or
            tablero[1]==tablero[4]==tablero[7] and tablero[1]!=' ' or
            tablero[2]==tablero[5]==tablero[8] and tablero[2]!=' ' or
            tablero[0]==tablero[4]==tablero[8] and tablero[0]!=' ' or
            tablero[2]==tablero[4]==tablero[6] and tablero[2]!=' '):
            print('El ganador es:  '+'X' if tx else 'El ganador es:  '+'O')
            juegofinal=True
        if ' ' not in tablero:
            print('Es un empate')
            juegofinal=True
        tx=not tx
        
   
else:
    print('Hasta la proxima')