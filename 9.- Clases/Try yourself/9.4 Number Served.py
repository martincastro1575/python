class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"\nThe Restaurant's name is: {self.restaurant_name.title()} and " 
                f"Its type is: {self.cuisine_type.title()}")
        
    def open_restaurant(self):
        print(f"Welcome to {self.restaurant_name} is open now!")
    
    def set_number_served(self, clients):
        if clients > self.number_served:
            self.number_served = clients
            print(f"\nNumber of clients: {self.number_served}")
        else:
            print(f"\nThe client's number must be bigger than {self.number_served}")
    
    def increment_number_served(self, increment_clients):
        
        if increment_clients > 0:
            self.number_served += increment_clients
            print(f"\nNumber of clients after increment: {self.number_served}")
        else:
            print("\nThe client's number must be different to zero value")


restaurant = Restaurant('mamma mia','italian food')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
print(f"\nNumber of clients: {restaurant.number_served}")


restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(35)


print("\n*****Incrementing the number of clients*****")
restaurant.increment_number_served(20)




# restaurant.number_served = 55
# print(f"\nNumber of clients: {restaurant.number_served}")


