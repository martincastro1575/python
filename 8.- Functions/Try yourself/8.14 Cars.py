def make_car(manufacturer, model_name, **details_car):
    details_car['manufacturer'] = manufacturer.title()
    details_car['model_name'] = model_name.title()

    return details_car

car = make_car('fiat companhy', 'siena fire 2.0', color = 'blue', tow_package= True, air_bag= True)

print("\Car Description: ")
print(car)