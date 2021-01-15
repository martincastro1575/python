from random import choice

class Lottery:
    def __init__(self):
        self.ticket = ''
        self.tokens = ('a','b','c','d','e',1,2,3,4,5) 
        self.times = 0

    def roll_machine(self):
        
        while self.times < 4:
            first_up = choice(self.tokens)
            self.ticket = self.ticket + str(first_up)
            self.times += 1
    
    def get_winner_ticket(self):
        print(f"\nThe winner ticket is: ***** {self.ticket.upper()} *****\n") 

t1 = Lottery()
t1.roll_machine()
t1.get_winner_ticket()