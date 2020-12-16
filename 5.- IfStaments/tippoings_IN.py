requested_toppings = ['Pinaple','strawberry','vanilla','chocolate','orange']

input_topping = 'vanilla'
flavor = input_topping in requested_toppings

if flavor:
    print(f"\nEl sabor '{input_topping}' se encuentra dentro de la lista de sabores")
else:
    print(f"\nEl sabor '{input_topping}' no se encuentra dentro de la lista de sabores")