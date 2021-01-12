class Dog:
    """ A simple attemppt to model a dog. """
    def __init__(self, name, age):
        """ Initialize name and age attributes. """
        self.name = name
        self.age = age
    
    def sit(self):
        """ Simulate a dog sitting in response to a command. """
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """ Simulate rolling over in response to a command. """
        print(f"{self.name} rolled over! ")

my_dog = Dog('Sasha', 7)
your_dog = Dog('Rocky', 9)

print(f"My dog's name is {my_dog.name.title()}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old")
my_dog.sit()