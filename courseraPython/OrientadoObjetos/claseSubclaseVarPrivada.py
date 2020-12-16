class Mapeo():
    def __init__(self, iterable):
        self.lista_de_items = []
        self.__actualizar(iterable)
    
    def actualizar(self, iterable):
        for item in iterable:
            self.lista_de_items.append(item)
    
    __actualizar = actualizar #copia privada de actualizar() original

class subClassMapeo(Mapeo):
    #provee una nueva signatura para actualizar()
    #pero no rompe __init__()
    def actualizar(self, keys, values):
        for item in zip(keys, values):
            self.lista_de_items.append(item)

