import car
import electric_car

my_fiat = car.Car('Fiat', 'Siena', 2020)
print(my_fiat.get_descriptive_name())

my_tesla = electric_car.ElectricCar('Tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())