def describe_city(city, country = 'Argentina'):
    print(f"\n{city.title()} is in {country.title()}")


describe_city('ciudad autonoma de buenos aires')
describe_city('mendoza')
describe_city('san juan')
describe_city(country = 'venezuela', city = 'vargas')