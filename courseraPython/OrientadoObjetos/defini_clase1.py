class MiClase():
    #atributo de clase
    i = 12345

    #metodo de clase
    def f(self):
        return 'Hola mundo'
    
    def g(self, msg='Hola Mundo'):
        return msg

first_class = MiClase()
second_class = MiClase()

first_class.i # 12345
first_class.f #Hola Mundo
second_class.g() #Hola Mundo
second_class.g("Nuevo mensaje") #Nuevo mensaje