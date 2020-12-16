cities = {
    'caracas': {
        'country': 'venezuela',
        'population': '6 millones',
        'superfice': '777 Km2',
    },
    'buenos aires capital':{
        'country': 'argentina',
        'population': '2.89 millones',
        'superfice': '203 Km2'
    },
    'monte video':{
        'country': 'uruguay',
        'population': '3.4 millones',
        'superfice': '176 Km2'
    }
}

for city, about in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\t Country: {about['country'].title()}, Population: {about['population']}, " 
               f"Superfice: {about['superfice']}")