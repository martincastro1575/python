def city_country(city, country):
    cit_coun = f'\n"{city.title()}, {country.title()}"'

    return cit_coun


print(city_country(city = "caracas", country = "venezuela"))
print(city_country(city = "santiago", country = "chile"))
print(city_country(city = "mendoza", country = "argentina"))