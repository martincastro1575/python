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