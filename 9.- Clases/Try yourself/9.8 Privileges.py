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

class Privileges():
    def __init__(self):
        self.privileges = []
    
    def set_privileges(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin's privileges: ")
        for privilege in self.privileges:
            print(f"-. {privilege}")


class Admin(User):
    def __init__(self, first, last, email, address):
        super().__init__(first, last, email, address)
        self.privileges = Privileges()    


admin_user = Admin('Martin','Castro','mjcm@gmail.com','CABA')
admin_user.privileges.set_privileges('can add post','can delete post','can ban user',
                                        'can be anything')
admin_user.greet_user()
admin_user.privileges.show_privileges()