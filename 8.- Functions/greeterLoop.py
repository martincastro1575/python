def get_formatted_name(firstname, lastname):
    """Display a simple greeting"""
    full_name = f"{firstname} {lastname}"

    return full_name.title()


while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' to exit)\n")

    f_name = input("First Name: ")
    if f_name.lower() == 'q':
        break

    l_name = input("Last Name: ")
    if l_name.lower() == 'q':
        break

    formatted_name = get_formatted_name(firstname = f_name, lastname = l_name)
    print(f"\nHello!!! {formatted_name}")