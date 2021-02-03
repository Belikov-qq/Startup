class Users():
    def __init__(self,f_name,l_name):
        self.first_name = f_name
        self.last_name = l_name
        self.login_attempts = 0

    def describe_user(self):
        print(
            "First name is " +
            self.first_name.title() + ",last name is " +
            self.last_name.title() + "."
        )
    def greet_user(self):
        print("Hi," + self.first_name.title() + self.last_name.title() + ".")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

us = Users('li','li')
us.increment_login_attempts()
us.increment_login_attempts()
print(us.login_attempts)
us.reset_login_attempts()
print(us.login_attempts)