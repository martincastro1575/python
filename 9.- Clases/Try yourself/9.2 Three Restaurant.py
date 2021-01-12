class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"\nThe Restaurant's name is: {self.restaurant_name.title()} and " 
                f"Its type is: {self.cuisine_type.title()}")
        

    def open_restaurant(self):
        print(f"Welcome to {self.restaurant_name} is open now!")

italian_restaurant = Restaurant('mamma mia','italian food')
mexican_restaurant = Restaurant('xapala', 'mexican food')
japaneese_restaurant = Restaurant('osaka', 'japaneese food')

italian_restaurant.describe_restaurant()
mexican_restaurant.describe_restaurant()
japaneese_restaurant.describe_restaurant()


