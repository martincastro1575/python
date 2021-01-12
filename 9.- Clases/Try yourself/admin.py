from user_only import User


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