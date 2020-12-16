favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'erin': 'c#',
    'martin': 'ruby',
}

print("\nThe following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(f"\t{language.title()}")


#Tambien se puede declarar un conjunto de esta manera, los conjuntos
#no muestran valores duplicados
#Un conjunto parece un diccionario pero no tiene la relacion clave-valor
languages = {'c','c#','python','java','c','python','java','javascript','c#'}
print("\nImprimiendo otro conjunto de datos:")
print(f"Conjunto de lenguajes de programacion: {languages}")
