prompt = "\nPlease enter a of toppings for you pizza"
prompt += "\nAnd enter 'q' to finish: "

while True:
    topping = input(prompt)

    if topping.lower() == 'q':
        break
    
    print(f"You added {topping.title()} topping ")