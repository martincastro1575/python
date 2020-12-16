favorite_places = {
    'german': {'river', 'beach', 'mountains'},
    'martin': {'lake', 'beach', 'forest'},
    'ana': {'bariloche', 'west coast'}
}

for name, places in favorite_places.items():
    print(f"\nThe favorite places of '{name.title()}' are:")
        
    for location in places:
        print(f"\t{location}")