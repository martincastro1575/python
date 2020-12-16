class CajaRegistradora(object):
    def calcular(self):
        pass

    #cuando el lector falla se registra el producto manual
    def ingresar_producto(self,codigo):
        pass

class Lector(object):
    def leer_codigo_barra(self):
        return

class Usuario(object):
    pass

class Cliente(Usuario):
    pass

class Cajero(Usuario):
    pass

class factura(object):
    pass

class Producto(object):
    
    def __init__(self, codigo, name, precio):
        self.codigo = codigo
        self.name = name
        self.precio = precio
    
    



bebida = Producto('11','Jugo de naranja',23)
#print(f"{bebida.codigo} - {bebida.name} - {bebida.precio}")