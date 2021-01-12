class User:
    def __init__(self, first, last, email, address):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.address = address
    
    def describe_user(self):
        print(f"\nSummary user's information: ")
        print(f"Firstname and Lastname: {self.first_name.title()} - {self.last_name.title()}")
        print(f"User's mail: {self.email.lower()}")
        print(f"user's address: {self.address.title()}")
    
    def greet_user(self):
        print(f"\nHellooo! {self.first_name.title()}, welcome to new job!!! ENJOY!")


user1 = User(
                'martin','castro',
                'martin.castro1575@gmail.com',
                'melincue, caba, villa del parque'
            )

user2 = User(
                'petra','perez',
                'petra.perez@gmail.com',
                'Juan B Justo, caba, villa del parque'
            )

user3 = User(
                'maria','castillo',
                'maria.castrillo@gmail.com',
                'Francisco Beiro, caba, villa del parque'
            )

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
    
