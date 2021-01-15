from random import choice

class Lottery:
    def __init__(self, ticket):
        self.ticket = ticket
        self.number_ticket = ''
        self.tokens = ('a','b','c','d','e',1,2,3,4,5) 
        self.times = 0
        self.repeat = 0

    def roll_machine(self):
        
        while self.times < 4:
            first_up = choice(self.tokens)
            self.number_ticket = self.number_ticket + str(first_up)
            self.times += 1

    def get_winner_ticket(self):
        
        while True:
            self.repeat += 1
            if self.ticket.upper() == self.number_ticket.upper():
                print(f"\nThe winner ticket is: ***** {self.number_ticket.upper()} *****\n")
                break
            
            self.times= 0
            self.number_ticket= ''
            self.roll_machine()

    def get_repeat(self):
        print(f"Cantidad de Intentos: {self.repeat}")        

t1 = Lottery('da1c')
t1.roll_machine()
t1.get_winner_ticket()
t1.get_repeat()