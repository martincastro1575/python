def make_pizza(*toppings):
    '''Print the list of toping pizza that have been requested'''
    """ Summarize the pizza we are about to make. """
    print("\nMaking pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
