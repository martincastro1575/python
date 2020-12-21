def describe_animal(animal_type, pet_name):
    '''Dispaly information about pet'''
    print(f"\nI have  a {animal_type.title()}")
    print(f"\nMy {animal_type.title()}'s name is {pet_name.title()}")

describe_animal('perro','sasha')
describe_animal('mouse','mickey')
describe_animal('clownfish','nemo')