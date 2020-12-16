"""Este programa tirara dos dados y sumara el resultado"""
import random
# esta funcion elige elige un numero entre 1 y 6
def TirarDado():
    Dado= int((random.random()*10%6)+1)  
    return Dado
# esta funcion suma los dos dados
def SumarDosDados(d1,d2):
    resultado = d1+d2
    return resultado
# esta funcion muestra en pantalla el resultado
def Resultado_a_mostrar():
    dado1,dado2= TirarDado(),TirarDado()
    print('El primer dado es:', dado1 ,'y el segundo es: ', dado2, 'la suma es ' ,SumarDosDados(dado1,dado2))
    
# funcion principal que cambia de mensaje depediendo si ya tiro una vez los dados    
def Sumar_Dos_Dados(a):
    if a == True:
        mensaje= input("¿quieres tirar los dados? presiona s para jugar o n para salir:")
    else:
        mensaje= input("¿Tirar otra vez? s/n:")
    while (mensaje == 's') or (mensaje == 'S'):
        a=False
        Resultado_a_mostrar()
        break
    while (mensaje == 'n') or (mensaje == 'N'):
        break
    else:
        Sumar_Dos_Dados(a)
 

def menu():
  primeratirada= True
  Sumar_Dos_Dados(primeratirada)   
    
 

menu()

