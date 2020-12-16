foods = ('Pizza','Pasta', 'Rice', 'Salad', 'Cereals')

print("\nMenu:")
for food in foods:
    print(f"\t{food}")

foods = ('Pizza','Pasta', 'Beaf', 'Beans', 'Cereals')

print("\n Update two Items in the Menu:")
for food in foods:
    print(f"\t{food}")

foods[1]="Ice Cream" #Esta linea generara un error, porq la tupla no se puede modificar