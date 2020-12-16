class Bolsa:
    def __init__(self, name):
        self.name = name
        self.datos = []
    
    def agregar(self, x):
        self.datos.append(x)
    
    def dobleagregar(self, x):
        self.agregar(x)

b = Bolsa('Bolsa Uno')
c = Bolsa('Bolsa Dos')
b.agregar('billetera')
c.dobleagregar('Lapiz labial')
print(f"{b.name} tiene en su interior una {b.datos}")
print(f"{c.name} tiene en su interior un {c.datos}")