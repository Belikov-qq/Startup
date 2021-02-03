class Restaurant():
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0
        self.login_attempts = 0

    def set_number_served(self,number):
        self.number_served = number
        print("This restaurant has served " + str(self.number_served) + " people.")

    def increment_number_served(self,number):
        if number >= 1:
            self.number_served += number
            print("I think it can sever " + str(self.number_served) + " people.")
        else:
            print("Error!")


my_res = Restaurant('Nick','China')
my_res.set_number_served(13)
my_res.increment_number_served(12)
my_res.increment_number_served(0)