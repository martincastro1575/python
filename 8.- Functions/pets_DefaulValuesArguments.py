def describe_animal(pet_name, animal_type = 'dog'):
    '''Dispaly information about pet'''
    print(f"\nI have  a {animal_type.title()}")
    print(f"\nMy {animal_type.title()}'s name is {pet_name.title()}")


describe_animal(pet_name = 'sasha')
describe_animal(animal_type = 'clownfish', pet_name ='marlyn')
describe_animal(pet_name = 'pluto')
describe_animal(pet_name = 'firulai')
describe_animal(animal_type = 'bird', pet_name = 'piolin')