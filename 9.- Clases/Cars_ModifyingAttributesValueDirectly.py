class Car:
    """ A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #Setting a default value for an Attribute

    def get_descriptive_name(self):
        """Return neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
    
        return long_name.title()
    
    def read_odometer(self):
        """Print a stament showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")


my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()