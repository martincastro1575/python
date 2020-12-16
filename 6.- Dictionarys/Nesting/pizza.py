#A List in a dictionary
#Store information about Pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extracheese']
}

#Summarize the order
print(f"\nYou ordered a pizza {pizza['crust']}-crust pizza "
        "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

