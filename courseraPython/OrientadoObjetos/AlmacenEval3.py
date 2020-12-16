import os


class CajaRegistradora(object):
    """Simula una caja registradora."""

    def __init__(self, d_123, d_124, d_125):
        """Inicializa los atributos para la caja registradora."""

        self.d_123 = (100 - float(d_123)) * 0.01  # Descuento para producto clave 123
        self.d_124 = (100 - float(d_124)) * 0.01  # Descuento para producto clave 124
        self.d_125 = (100 - float(d_125)) * 0.01  # Descuento para producto clave 125
        self.producto = {123: ['Manzana', 30*self.d_123], 124: ['Pasta Dental', 70*self.d_124],
                         125: ['Pila', 15*self.d_125]}  # Ingreso los codigos de los productos y aplica los descuentos.
        self.lista_compra = []
        self.suma = 0

    def muestro_codigos(self):
        """Imprimo en pantalla los códigos de los productos."""
        print('Producto:    Codigo:')
        print('----------------------')
        for i in self.producto.keys():
            print(self.producto[i][0], "-->", i)

    def lista_comprador_update(self, codigo):  # Actualizo la lista del comprador
        """Ingreso los productos del consumidor a una lista aparte para luego sumar sus precios."""
        codigo = int(codigo)  # Es el codigo que ingreso del producto.
        try:
            self.lista_compra.append(self.producto[codigo])  # Agrego el producto ingresado a la lista del comprador.
            print('Producto:      Precio:')
            for i in range(len(self.lista_compra)):
                print(self.lista_compra[i][0], ": $", self.lista_compra[i][1])
        except KeyError:
            print('El codigo no se encuentra registrado.')

    def suma_productos_comprados(self):
        """Suma los precios de los productos que se van agregando a la lista del comprador."""
        self.suma = 0
        for i in self.lista_compra:
            self.suma += i[1]

    def muestra_subtotal(self):
        """Muestra el subtotal a medida que se agrega un producto."""
        print('Subtotal: $', self.suma)

    def muestra_total(self):
        """Muestra la suma total que tiene que pagar el comprador."""
        print('Total: $', self.suma)
        return self.suma

    def cambio(self, paga):
        """Muestra cuanto es el vuelto al comprador."""
        vuelto = paga - self.suma
        print('El vuelto es de $', vuelto)


while True:
    print('Ingrese un numero del 0 al 100%.')
    try:
        d_1 = int(input('ingrese el descuento de las Manzanas:'))
        d_2 = int(input('ingrese el descuento de la Pasta Dental:'))
        d_3 = int(input('ingrese el descuento de la Pila:'))
        break  # Sale del "while" si los descuentos ingresados son validos.
    except ValueError:
        print('ESO NO ES UN DESCUENTO VALIDO.Ingrese un numero valido del 0 al 100.')
        continue  # Repite el while si uno de los descuentos no es valido.
producto_1 = CajaRegistradora(d_1, d_2, d_3)  # Instancia de la clase 'CajaRegistradora'
while True:
    os.system('cls')  # Limpia la pantalla.
    producto_1.muestro_codigos()  # Muestro los codigos de cada producto
    prod = input('Ingrese el codigo del producto:')
    producto_1.lista_comprador_update(prod)  # Va mostrando la lista del comprador.
    producto_1.suma_productos_comprados()  # Suma los productos que fueron agregados a la lista.
    producto_1.muestra_subtotal()        # Muestra el subtotal.
    salir = input('Apriete "Y" para salir. Apriete cualquier tecla para seguir ingresando productos:')
    if salir.upper() == "Y":
        os.system('cls')  # Limpia la pantalla.
        break  # Sale del while
    else:
        continue  # Continua ingresando productos
producto_1.muestra_total()  # Muestra el total a pagar.
paga_con = int(input('Ingrese con cuanto paga el comprador:'))
producto_1.cambio(paga_con)  # Muestra el vuelto que se le debe al comprador.
input()