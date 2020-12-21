def make_pizza(size, *toppings):
    '''Print the list of toping pizza that have been requested'''
    """ Summarize the pizza we are about to make. """
    print(f"\nMaking a {size}-inc pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza(6,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
