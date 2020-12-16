first_name = 'Martin'
last_name = 'Castro'
full_name = f'{first_name} {last_name}'
print(f'Hello! {full_name.title()}!!!')

message = f'Hello! {full_name.title()}!!!'
print('Mensaje formateado en variable: ', message)

full_name_dos = '{} {}'.format(first_name, last_name)
print('Otra manera de formatear un mensaje:', full_name_dos)

print('Agregando tabulacion y saltos de linea: \n')
print('Languages:\n\tPython\n\tC\n\tJavaSript')

print('Elmiminando espacios en blanco del lado derecho')
language = 'Python'
print('String original:',language)
language = language.rstrip()
#Tambien puedes usar la funcion lstrip() para elmiminar caracteres en 
#blanco a la izquierda y strip() para eliminar caracteres en blanco 
#en ambos extremos del estring.

print('Sin espacios a la derecha: ',language)