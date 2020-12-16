#Caja registradora para un almacÃ©n. 
# 
# El sistema debe poder escanear un producto (el cajero puede tipear el cÃ³digo del producto)
# Agregarlo a la lista de productos comprados para ese cliente.
# Mostrar el subtotal. 
# El cajero cuando lo desee puede finalizar la compra y el sistema deberÃ¡ aplicar los descuentos correspondientes a los productos. 
# Luego, el cajero indica con cuÃ¡nto paga el cliente y el sistema debe mostrar el cambio que debe devolver al cliente.

import os
import unittest

#opcion = 'x'
vuelto = 0
class producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class compra:
    def __init__(self, codigo, cantidad):
        self.codigo = codigo
        self.cantidad = cantidad

class caja_registradora(object):
    #Preparacion del sistema
    listaProductos = []
    listaCompra = []


    #Carga una lista con 4 productos
    def __init__(self):
        self.listaProductos.append(producto('001','Manzana', 40))
        self.listaProductos.append(producto('002','Arroz', 7))
        self.listaProductos.append(producto('003','Mayonesa', 50))
        self.listaProductos.append(producto('004','Sal', 30))

    #Menues del sistema
    def mostrarMenuPrincipal():
        """Muestra el menu en pantalla"""
        os.system('cls')
        print("\n")
        print("MENU".center(14,"-"))
        print("1.Ingresar Compra")
        print("2.Lista de productos")
        print("")
        print("Q.Salir ")

    def mostrarMenuCompra():
        """Muestra el menu de la opcion 1"""
        os.system('cls')
        print("\n")
        print("MENU Ingreso de Compra".center(14,"-"))
        print("A.Ingresar Productos")
        print("L.Ver Lista de Compra Actual")
        print("F.Facturar")
        print("")
        print("V.Volver ")

    def mostrarMenuLista():
        """Muestra el menu en pantalla"""
        print("\n")
        print("MENU".center(14,"-"))
        print("I.Ingresar Producto nuevo")
        print("L.ver lista de productos")
        print("")
        print("v.Volver ")

    # El sistema debe poder escanear un producto (el cajero puede tipear el cÃ³digo del producto)
    # Agregarlo a la lista de productos comprados para ese cliente.
    # Mostrar el subtotal. 
    def ingresoCompra():
        os.system('cls')
        codigo=input("\nIngrese un Codigo de Producto o C para Cancelar: ")
        while codigo != 'c':
            cantidad=int(input("Cantidad: "))
            os.system('cls')
            caja.listaCompra.append(compra(codigo,cantidad))
            subtotal = 0
        
            for objC in caja.listaCompra:
                for objP in caja.listaProductos:
                    if objC.codigo == objP.codigo:
                        subtotal = subtotal + (int(objP.precio) * int(objC.cantidad))
                        print(objP.codigo, objP.nombre, objP.precio, objC.cantidad,  sep = ' ')
            print("\nEl subtotal es: $", subtotal)
            codigo=input("\nIngrese un Codigo de Producto o C para Cancelar: ")
        else:
            pass

    def ingresoCompraTest(self,codigo,cantidad):
        self.listaCompra.append(compra(codigo,cantidad))
        return    

    subtotal= 0
    def finalizarCompra(self):    
        for objC in self.listaCompra:
            for objP in self.listaProductos:
                if objC.codigo == objP.codigo:
                    self.subtotal = self.subtotal + (int(objP.precio) * int(objC.cantidad))
                    print(objP.codigo, objP.nombre, objP.precio, objC.cantidad,  sep = ' ')
        print("\nEl subtotal es: $", self.subtotal)
        return self.subtotal
    
    
    
    def generoFactura(self,pago,cliente):
        # Aplico un descuento del 10% si es cliente registrado
        if cliente == 's':
            self.subtotal = self.subtotal - (self.subtotal * 0.01)
            return pago - self.subtotal
        else:
            return pago - self.subtotal


    def mostrarListaCompra():
        subtotal = 0
        os.system('cls')
        print("\nLista de compra actual")
        if len(listaCompra) == 0:
            print("\nLa lista de compra estÃ¡ vacia.")
        else:
            for objC in listaCompra:
                for objP in listaProductos:
                    if objC.codigo == objP.codigo:
                        subtotal = subtotal + (int(objP.precio) * int(objC.cantidad))
                        print(objP.codigo, objP.nombre, objP.precio, objC.cantidad,  sep = ' ')
            print("\nEl subtotal es: $", subtotal)
        opcion=input("\nPresione V para volver: ")

    # El cajero cuando lo desee puede finalizar la compra y el sistema deberÃ¡ aplicar los descuentos correspondientes a los productos. 
    # Luego, el cajero indica con cuÃ¡nto paga el cliente y el sistema debe mostrar el cambio que debe devolver al cliente.
    def generarFactura():
        cuenta = 0
        os.system('cls')
        print("\nResumen de Compra\n")

        for objC in listaCompra:
            for objP in listaProductos:
                if objC.codigo == objP.codigo:
                    print(objP.codigo, objP.nombre, objP.precio, objC.cantidad,  sep = ' ')
                    cuenta = cuenta + (int(objP.precio) * int(objC.cantidad))
        print("\nLa cuenta es: $", cuenta)
        
        cliente= input("Es cliente registrado? (S/N): ")

        if cliente == 's':
            print("\nPor ser cliente registrado obtiene un 10% de descuento en su compra.\n")
            cuenta = cuenta - (cuenta * 0.01)
            print("La cuenta con descuento es: $", cuenta)
        else:
            print("\nSi Usted fuera un cliente registrado hubiera tenido un descuento de: $", (cuenta * 0.01))
            
        pago = int(input("\nIngrese su pago: "))
        while pago < cuenta:
            print("El monto ingresado es insuficiente.")
            pago = int(input("\nIngrese su pago: "))
        else:
            print("\nSu vuelto es: $", round(pago - cuenta))
            
            listaCompra[:] = []
            opcion=input("\nPresione V para volver: ")
            mostrarMenuPrincipal()

    #Se pueden agregar productos a la lista pre cargada (faltan realizar validaciones de codigos repetidos)
    def ingresoProducto():
        codigo=input("Codigo: ")
        nombre = input("Nombre: ")
        precio = int(input("Precio: "))
        listaProductos.append(producto(codigo,nombre,precio))

    def mostrarLista():
        os.system('cls')
        print("\nLista de Productos")
        print("\nCodigo | Nombre | Precio")
        for obj in listaProductos:
            print(obj.codigo, obj.nombre, obj.precio, sep = '   ')
        mostrarMenuLista()    
   
#MAIN faltan validaciones de ingresos incorrectos



##########Test#########


class caja_Registradora_Test(unittest.TestCase):
    def setUp(self):    
        #Declaro el objeto
        self.objCajaTest = caja_registradora
        

        #Cargo la lista de productos en inventario
        self.objCajaTest.listaProductos.append(producto('001','Manzana', 40))
        self.objCajaTest.listaProductos.append(producto('002','Arroz', 7))
        self.objCajaTest.listaProductos.append(producto('003','Mayonesa', 50))
        self.objCajaTest.listaProductos.append(producto('004','Sal', 30))

    #Simulo agregar un producto a la lista
    def test_01_(self):
        self.objCajaTest.ingresoCompraTest(self.objCajaTest,'001',1)
        self.assertEqual(self.objCajaTest.listaCompra[0].codigo, '001')

    #Simulo cerrar la compra y verifico que el subtotal sea 80
    def test_0_(self):
        self.objCajaTest.subtotal = self.objCajaTest.finalizarCompra(self.objCajaTest)
        self.assertEqual(self.objCajaTest.subtotal, 120)
    
    #Simulo generar la factura para un cliente Registrado (Descuento de 10%) y no registrado
    def test_03_(self):
        #El cliente pago con 130 y esta registrado, vuelto 100
        self.objCajaTest.vuelto = self.objCajaTest.generoFactura(self.objCajaTest,100,'s')
        self.assertEqual(self.objCajaTest.vuelto, 100)

        #El cliente pago con 130 y No esta registrado, vuelto 100
        self.objCajaTest.vuelto = self.objCajaTest.generoFactura(self.objCajaTest,100,'n')
        self.assertEqual(self.objCajaTest.vuelto, 100)


if __name__ == '__main__':
    unittest.main()