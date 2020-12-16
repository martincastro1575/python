favorite_number = {
    'maria': [5,4,67], 
    'juana': [7,23,40,9], 
    'petra': [87,33,13,15],
    'juan' : [1],
    }
    
for name, numbers in favorite_number.items():
    suma = 0
    if len(numbers) > 1:
        texto = 'are'
    else:
        texto = 'is'

    print(f"\nThe favorite numbers of {name} {texto}:")
    for number in numbers:
        suma += number
        print(f"\t{number}")
    print(f"\tY las suma de los numeros: {suma}")