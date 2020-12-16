class Perro():
    tipo = 'canino' #variable de clase, compartida por todas las instancias

    def __init__(self, nombre):
        self.nombre = nombre #variable de instancia, unica para la instancia

d = Perro('Fifi')
e = Perro('Firulai')
print(d.nombre) #variable unica para la instancia (d)
print(e.nombre) #variable unica para la instancia (e)

#variable compartida para las instancias (d) y (e)
print(d.tipo)
print(e.tipo)