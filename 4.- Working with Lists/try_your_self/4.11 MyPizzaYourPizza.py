my_pizzas = ['blue cheese', 'pepperoni', 'hawaina', 'meat and pork']
your_pizzas = my_pizzas[:]

print(f"My favorite Pizzas are: {my_pizzas}")
print(f"Your favorite Pizzas are: {your_pizzas}")

my_pizzas.append('jam and cheesse')
your_pizzas.append('Mozarella')

print(f"\nMy new favorite Pizzas are :")
for pizza in my_pizzas:
    print(f"\t{pizza}")

print(f"\nYour new favorite Pizzas are :")
for pizza in your_pizzas:
    print(f"\t{pizza}")