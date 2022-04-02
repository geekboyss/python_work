class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print(full_name.title())
    
    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hello " + full_name.title())

class Admin(User):
    def __init__(self, first_name, last_name, *privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


user1 = Admin('Geek', 'boy', "can add post", "can delete post")
user1.describe_user()
user1.greet_user()
user1.show_privileges()
