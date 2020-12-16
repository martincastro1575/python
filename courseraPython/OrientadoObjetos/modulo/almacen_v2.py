import unittest

class DineroInsuficiente(Exception):
    pass

class ProductoInexistente(Exception):
    pass

class CompraNoFinalizada(Exception):
    pass

class CajaRegistradora(object):
    def __init__(self, producto, lista_precio):
        self.producto = producto
        self.lista_precio = lista_precio
        self.compra = Comprar()
    
    def leer_producto(self, codigo):
        producto = producto.codigo
        if not producto == codigo():
            raise ProductoInexistente("El producto no existe")
        return producto

    def agregar_producto(self, codigo):
        producto = self.leer_producto(codigo)
        self.ini_compra().agregar_producto(producto)
    
    def ini_compra(self):
        return self.ini_compra

    def calcular_subtotal(self):
        subtotal = 0
        lista_product = self.ini_compra().products()
        for product in lista_product:
            subtotal +=  self.lista_precio.precio_prod

        return subtotal
    
    def terminar_compra(self):
        self.ini_compra().off_compra()

    def total(self):
        if self.ini_compra().off_compra():
            raise CompraNoFinalizada("La compra sigue abierta")
        total = 0
        lista_product = self.ini_compra().products()
        for product in lista_product:
            total += self.lista_precio.precio_prod
        
        return total
    
    def pagar(self, dinero):
        total = self.total()
        
        if dinero < total:
            raise DineroInsuficiente("Falta dinero para completar la compra")

        return dinero - self.total()

class Comprar(object):
    def __init__(self):
        self.products = []
        self.fin_compra = False
        
    def product(self):
        return self.products

    def ingresar_product(self, producto):
        self.products.append(producto)
    
    def off_compra(self):
        self.fin_compra = True
        return self.fin_compra


class Product(object):    
    def __init__(self, codigo, name):
        self.codigo = codigo
        self.name = name
    
    def codigo(self):
        return sel.codigo
    
    def name(self):
        return name

class ListaPreciosDescuento(object):
    def __init__(self):
        self.list_precio_producto = {}
        self.list_descuento_producto = {}

    def precio_prod(self, codigo):
        return self.list_precio_producto[codigo]
    
    def descuento_prod(self, codigo):
        precio_prod = self.list_precio_producto[codigo]
        descuento_prod = self.list_descuento_producto.get(codigo,0)
        prod_prec_desc = precio_prod * descuento_prod
        return precio_prod - prod_prec_desc
    
    def aplicar_precio(self, codigo, precio):
        self.list_precio_producto[codigo] = precio
    
    def aplicar_descuento(self, codigo, descuento):
        self.list_descuento_producto[codigo] = descuento
    


class CajaRegistradoraTest(unittest.TestCase):
    #preparando al objeto
    def setUp(self):
        product_one = Product('PEP01','Carne')
        product_dos = Product('PEP02', 'Pollo')
        product_tres = Product('PEP03','Papa')
        self.producto = [product_one, product_dos, product_tres]

        self.lista_precio = ListaPreciosDescuento()
        self.lista_precio.aplicar_precio(product_one, 400)
        self.lista_precio.aplicar_precio(product_dos, 110)
        

        self.cajaregistradora = CajaRegistradora(producto = self.producto, lista_precio = self.lista_precio)

    def test_agregar_inexistente(self):
        cajaregistradora = CajaRegistradora(producto=[], lista_precio=ListaPreciosDescuento())
        codigo_pro = 'PEP04'

        self.assertRaises(ProductoInexistente, cajaregistradora.agregar_producto, codigo_pro)

    def test_agregar_producto_existente(self):
        codigo_pro = 'PEP01'
        producto = self.cajaregistradora.agregar_producto(codigo_pro)

        self.assertEqual(1, len(self.cajaregistradora.ini_compra().products()))
        self.assertEqual('PEP02', self.cajaregistradora.ini_compra().products()[0].codigo())

    def test_fondo_insuficiente(self):
        codigo_pro = 'PEP03'
        poducto = self.cajaregistradora.agregar_producto(codigo_pro)
            
        self.cajaregistradora.terminar_compra()
        self.assertEqual(200, self.cajaregistradora.total())
        self.assertRaises(DineroInsuficiente, self.cajaregistradora.pagar, 50)
        
    def test_compra_no_finalizada(self):
        codigo_pro = 'PEP03'
        producto = self.cajaregistradora.agregar_producto(codigo_pro)
        self.assertRaises(CompraNoFinalizada, self.cajaregistradora.total)
    
    def test_producto_sin_descuento(self):
        codigo_pro = 'PEP01'
        producto = self.cajaregistradora.agregar_producto(codigo_pro)
        self.cash_register.finish_purchase()
        self.assertEqual(10.00, self.cash_register.total())
        

if __name__ == '__main__':
    unittest.main()