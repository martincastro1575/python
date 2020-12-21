def get_formatted_name(first_name, last_name, middle_name = ''):
    '''Returned fullname, neatly formatted'''
    if middle_name:
        fullname = f"{first_name} {middle_name} {last_name}"
    else:
        fullname = f"{first_name} {last_name}"

    return fullname.title()


musician = get_formatted_name('Jimmy', 'Hendrix')
print(f"\nMucician's name is: {musician}\n")

musician = get_formatted_name('John', 'Lee', 'Hooker')
print(f"\nMucician's name is: {musician}\n")


