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
    
    #Modifing an attrubute's value through a Method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
           Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    #Incrementing an Attribute's value through a Method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't input miles less than 0")
    
    def fill_gas_tank(self):
            """ Cars have gas tanks. """
            print("\nThis car need a gas tank!")

class Battery():
    """ A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size= 75):
        """ Initialize the batery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """ Print a stament describing the baterry size """
        print(f"This car has a {self.battery_size}-KWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        elif self.battery_size > 75 & self.battery_size < 100:
            range = 290
        
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
        """ Represent aspects of a car, specific to electric vehicles. """
        def __init__(self, make, model, year):
            """ Initialize attributes of the parent class. """
            super().__init__(make, model, year)
            self.battery = Battery(75)

        
        def fill_gas_tank(self):
            """ Electric cars don't have gas tanks. """
            print("\nThis car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', '2019')
my_gas_car = Car('Fiat', 'Siena 2020', '2020')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
