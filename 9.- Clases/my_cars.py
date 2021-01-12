from car import Car
from electric_car import ElectricCar

my_fiat = Car('Fiat', 'Siena', 2020)
print(my_fiat.get_descriptive_name())

my_tesla = ElectricCar('Tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())