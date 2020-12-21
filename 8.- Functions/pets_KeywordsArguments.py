def describe_animal(animal_type, pet_name):
    '''Dispaly information about pet'''
    print(f"\nI have  a {animal_type.title()}")
    print(f"\nMy {animal_type.title()}'s name is {pet_name.title()}")

describe_animal(pet_name ='sasha', animal_type = 'perro')
describe_animal(animal_type = 'clownfish', pet_name ='marlyn')