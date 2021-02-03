class Users():
    def __init__(self,f_name,l_name):
        self.first_name = f_name
        self.last_name = l_name

    def describe_user(self):
        print(
            "First name is " +
            self.first_name.title() + ",last name is " +
            self.last_name.title() + "."
        )
    def greet_user(self):
        print("Hi," + self.first_name.title() + self.last_name.title() + ".")

user1 = Users('Nick','Young')
user1.describe_user()
user1.greet_user()