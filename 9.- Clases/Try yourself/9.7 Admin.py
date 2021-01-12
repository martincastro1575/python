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

class Admin(User):
    def __init__(self, first, last, email, address):
        super().__init__(first, last, email, address)

    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"Admin's privileges: ({self.first_name} - {self.last_name})")
        for privilege in self.privileges:
            print(f"-. {privilege}")


privileges = ['can add post','can delete post','can ban user']

admin_user = Admin(privileges)
admin_user.first_name = 'Martin'
admin_user.last_name = 'Castro'
admin_user.show_privileges()