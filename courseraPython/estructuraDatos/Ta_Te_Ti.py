#contenido inicial de matriz
matriz = [['_','_','_'],['_','_','_'],['_','_','_']]

def dibujar_matriz():    
    for fila in range(3):
        print('|',matriz[fila][0],'|',matriz[fila][1],'|',matriz[fila][2],'|')
    
    return

def iniciar_juego():
    #Dibuja la matriz
    while True:        
        ficha = input("Ingrese la letra X para jugar con la ficha (X) o la letra O para jugar con la ficha (O): ")
        if ficha in ['X','x','o','O']:            
            fic_aux = ficha.upper()
            print(f'Usted selecciono {fic_aux} al otro jugador le corresponde la ficha restante\n')
            break        
        else:
            print("Ingrese la letra 'X' o la letra 'O', para iniciar el juego")
    
    #Inicia el juego
    cond = True
    tabla = 0
    while cond:
        #captura el error
        try:
            print(f"Es el turno de la ficha ({fic_aux})")
            f = int(input("Ingrese fila: "))
            c = int(input("Ingrese columna: "))
            tabla += 1                   
        except ValueError:
            print("Debe ingresar un valor numerico.\n")
            dibujar_matriz()
        else:
            if c >=0 and c < 3 and f >=0 and f < 3:
                if matriz[f][c] != '_':
                    print(f"La posicion {f} - {c} esta ocupada por {matriz[f][c]} ")
                    dibujar_matriz()
                    tabla -= 1     
                else:                    
                    matriz[f][c]= fic_aux
                    dibujar_matriz()                

                    #evalua las diagonales
                    if (matriz[f][c] ==  matriz[0][0] and matriz[f][c] == matriz[1][1] and matriz[f][c] == matriz[2][2]) or (matriz[f][c] ==  matriz[0][2] and matriz[f][c] == matriz[1][1] and matriz[f][c] == matriz[2][0]):
                        fic_aux = matriz[f][c]
                        cond = False
                    elif tabla == 9:
                        fic_aux = 'Empate'
                        cond=False
                    else:
                        #evalua las filas
                        for fil in range(3):
                            if matriz[fil].count(fic_aux) == 3:
                                print(f"El gandador es ({fic_aux})\n")
                                cond = False
                    
                        #evalua las columnas
                        for col in range(3):
                            aux_col=[]
                            for fil in range(3):
                                aux_col.append(matriz[fil][col]) 
                                if aux_col.count(fic_aux) == 3:
                                    cond = False
                                    break     
                    #Intercambia las ficha
                    if fic_aux == 'O' and cond == True:
                        fic_aux = 'X'
                    elif fic_aux == 'X' and cond == True:
                        fic_aux = 'O'
            else:
                print('Los valores para las fila y columnas deben estar entre cero (0) y dos (2)')
    return fic_aux


print("\n\t\t\tReglas del Juego (TA-TE-TI) :\n",
        "\t1.- La fichas seran (X) o (O).\n",
        "\t2.- Cada jugador tiene una oportunidad de juego.\n",
        "\t3.- Se debe indicar un valor entre 0 y 2 para las filas.\n",
        "\t4.- Se debe indicar un valor entre 0 y 2 para las columnas.\n",
        "\t5.- La combinacion fila-columna ubicar la ficha en esa combinacion.\n")

dibujar_matriz()
print("\nPara iniciar el juego, debe ingresar la posicion horizontal\n",
      "para las filas y la vertical para las columnas")
   

print(f"El ganador del juego es: {iniciar_juego()}\n")

