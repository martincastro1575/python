from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.times = 0

    def roll_die(self):
        print(f"\nSides: {self.sides}")
        while self.times < 10:
            self.times += 1
            print(randint(1, self.sides))

sides_6 = Die(6)
sides_6.roll_die()

sides_10 = Die(10)
sides_10.roll_die()

sides_20 = Die(20)
sides_20.roll_die()


            
