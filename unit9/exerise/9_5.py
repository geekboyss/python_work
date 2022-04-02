class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print(full_name.title() + " " + str(self.login_attempts))
    
    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hello " + full_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Geek', 'boy')
user1.describe_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

user1.describe_user()

user1.reset_login_attempts()

user1.describe_user()
