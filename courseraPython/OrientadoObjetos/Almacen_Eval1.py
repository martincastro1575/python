class CajaReg:

    def __init__(self, a=0, r=0, recibido=0, cambio=0, temp=0):

        print("\n\n*****BIENVENIDO A NUESTRO SUPERMERCADO*****\n")

        self.a = a
        self.r = r
        self.recibido = recibido
        self.cambio = cambio
        self.temp = temp

    def prods(self):
        print("*****AC SUPERMERCADO*****")
        print("1. Producto 1 -----> 10", "\n2.Producto 2----->25", "\n3.Prodcuto 3--->45", "\n4.Producto 4---->70","\n5.Subtotal", "\n6.Exit")
        while (1):
            c = int(input("Elegir una opciÃ³n:\n"))
            if (c == 1):
                d = int(input("Por favor ingrese la cantidad:\n"))
                self.r = self.r + 30 * d
            elif (c == 2):
                d = int(input("Por favor ingrese la cantidad:\n"))
                self.r = self.r + 35 * d
            elif (c == 3):
                d = int(input("Por favor ingrese la cantidad:\n"))
                self.r = self.r + 50 * d
            elif (c == 4):
                d = int(input("Por favor ingrese la cantidad:\n"))
                self.r = self.r + 40 * d
            elif (c == 5):
                print("total:", self.r)
                if (self.r > 0):
                    recibido = int(input("Por favor ingrese el dinero recibido:\n"))
                    print("Cambio:", recibido - self.r)
                    print("*****Gracias por preferirnos, te esperamos pronto!!!*****")
                    quit()
            elif (c == 6):
                quit()
            else:
                print("OpciÃ³n invalida")

def main():
    a = CajaReg()
    while (1):
            a.prods()
main()
