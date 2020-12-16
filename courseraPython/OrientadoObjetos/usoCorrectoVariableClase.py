class Perro():
    

    def __init__(self,nombre):
        self.nombre = nombre
        self.trucos = [] #uso correcto de la variable de instancia

    def agregar_trucos(self, truco):
        self.trucos.append(truco)
    
d = Perro('Fifi')
e = Perro('Firulai')

d.agregar_trucos('Girar')
e.agregar_trucos('Dar la Pata')
print(d.nombre) #variable unica para la instancia (d)
print(e.nombre) #variable unica para la instancia (e)

#imprime los mismos trucos para ambos perro, lo cual es incorrecto porq cada
#perro puede tener un truco particular o pueden o no compartir trucos.
print(f"Trucos de {d.nombre}: {d.trucos}")
print(f"Trucos de {e.nombre}: {e.trucos}")