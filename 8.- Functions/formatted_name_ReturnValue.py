def get_formatted_name(first_name, last_name):
    '''Returned fullname, neatly formatted'''
    fullname = f"{first_name} {last_name}"

    return fullname.title()


musician = get_formatted_name('jimix', 'hendrix')
print(f"\nMucician's name is: {musician}\n")

