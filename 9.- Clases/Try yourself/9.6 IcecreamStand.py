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
        if clients > 0:
            self.number_served = clients
        else:
            print("\nThe client's number must be different to zero value")
    
    def increment_number_served(self, increment_clients):
        
        if increment_clients > 0:
            self.number_served += increment_clients
        else:
            print("\nThe client's number must be different to zero value")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def set_flavors(self,*flavors):
        self.flavors = flavors

    def get_flavors(self):
        for flavor in self.flavors:
            print(f"Ice Cream of {flavor} flavor")
    



#flavors = ['Vainilla', 'Strawberry','apple','banana','grapes']
ice_restaurant = IceCreamStand('Freedo','Ice Cream Store')
ice_restaurant.set_flavors('Vanilla','banana split', 'pistache', 'nutella')
ice_restaurant.describe_restaurant()
ice_restaurant.get_flavors()