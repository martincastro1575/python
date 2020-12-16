def smart_division(div_func):
    def div(a,b):
        if b == 0:
            print("No se puede dividir entre cero (0)")
            return
        return div_func(a,b)
    return div

@smart_division
def division(a,b):
    return a/b

division(1,2)
division(2,0)

def log(f):
    def wrap(*args, **kwargs):
        print("Ejecutando la funcion", f.__name__,
        "con los argumentos", ", ".join([str(arg) for arg in args]))
        return f(*args, **kwargs)
    return wrap

@log
def suma(a,b):
    return a + b

suma(1,2)

@log
@smart_division
def division_2(a,b):
    return a/b

division_2(1,2)
division_2(2,0)