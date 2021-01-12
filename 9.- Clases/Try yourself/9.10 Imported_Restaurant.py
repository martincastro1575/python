from restaurant import Restaurant,IceCreamStand
#flavors = ['Vainilla', 'Strawberry','apple','banana','grapes']
italian_restaurant = Restaurant('Mamma mia', 'Italian')
italian_restaurant.describe_restaurant()

ice_restaurant = IceCreamStand('Freedo','Ice Cream Store')
ice_restaurant.set_flavors('Vanilla','banana split', 'pistache', 'nutella')
ice_restaurant.describe_restaurant()
ice_restaurant.get_flavors()