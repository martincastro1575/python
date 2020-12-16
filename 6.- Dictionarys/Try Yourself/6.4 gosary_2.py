glosarys = {'get': 'obtener un valor del diccionario',
            'print': 'imprimir un valor en pantalla',
            'upper': 'Convertir un string en mayusculas',
            'lower': 'Convertir un string en minusculas',
            'set' : 'Crea un conjunto de valores sin duplicados',
            '[:]' : 'Sirve para copiar una lista'
          }

print("\nGlosario de Python:")
for command, description in glosarys.items():
  print(f"\tComando: {command}, Description: {description}")

