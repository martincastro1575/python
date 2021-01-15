class User:
    def __init__(self, first, last, email, address):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.address = address
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"\nSummary user's information: ")
        print(f"First name and Lastname: {self.first_name.title()} - {self.last_name.title()}")
        print(f"User's mail: {self.email.lower()}")
        print(f"user's address: {self.address.title()}")
    
    def greet_user(self):
        print(f"\nHellooo! {self.first_name.title()}, welcome to new job!!! ENJOY!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    
    def get_login_attemps(self):
        return self.login_attempts


user1 = User(
                'martin','castro',
                'martin.castro1575@gmail.com',
                'melincue, caba, villa del parque'
            )

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"\nNumber of login attempts: {user1.get_login_attemps()}")

print("\n*****Reset Login Attempts*****")
user1.reset_login_attempts()
print(f"Number of login attempts: {user1.get_login_attemps()}")
