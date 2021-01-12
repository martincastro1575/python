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
    
    def call_incremented(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0