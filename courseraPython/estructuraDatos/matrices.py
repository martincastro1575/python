#definicion de una matriz 3 x 4
matriz = [[1,2,3,4,5],[5,6,7,8,9,5],[9,10,11,12,5]]

#Accesando a elementos
matriz[0][0] #1
matriz[1][2] #7

#Ejemplo de funcion de suma de matrices

def suma_matrices(A,B):
    #Las matrices A y B son del mismo tamaño
    cant_filas = len(A)
    cant_cols = len(A[0])
    print(f"Filas: {cant_filas}, Columnas: {cant_cols}")

    C=[]

    for fila in range(cant_filas):
        fila_suma = []

        for col in range(cant_cols):
            fila_suma.append(A[fila][col] + B[fila][col])  
        C.append(fila_suma)
    
    return C


print(suma_matrices(matriz,matriz))