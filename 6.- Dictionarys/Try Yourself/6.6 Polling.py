favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'annette': '.net',
    'maria': 'js',

}

people = ['jen','jose','sarah','pedro','annette','carlos','maria']

print("People take the poll!!!\n")
for person in people:
    
    if person in favorite_languages.keys():
        print(f"\t{person}! thanks for take the poll")
    else:
        print(f"\t\t{person}! please you should take the poll...")



