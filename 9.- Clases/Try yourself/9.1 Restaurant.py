class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"\nThe Restaurant's name is: {self.restaurant_name.title()} and " 
                f"Its type is: {self.cuisine_type.title()}")
        

    def open_restaurant(self):
        print(f"Welcome to {self.restaurant_name} is open now!")

restaurant = Restaurant('mamma mia','italian food')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()