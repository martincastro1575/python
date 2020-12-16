requested_toppings = []

#validamos que la lista tengo al menos un item
#devuelve True si tiene al menos un elemento y False
#sino tiene elementos
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("\nSorry, we are out of green peppers rigt now.")
        else:
            print(f"\nAdding {requested_topping}.")
        
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

