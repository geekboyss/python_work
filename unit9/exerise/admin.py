from userr import User

class Admin(User):
    def __init__(self, first_name, last_name, *privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for pl in self.privileges:
            print(pl)
