class Restaurant():
    def __init__(restauran,name,type):
        restauran.name = name
        restauran.type = type

    def describe_restaurant(restaurant):
        print(restaurant.name.title() + " is a " + restaurant.type.title() + "restaurant.")

    def open_restautant(restaurant):
        print(restaurant.name.title() + " is open for business.")

my_res = Restaurant('Nick','Chiniese')
my_res.describe_restaurant()
my_res.open_restautant()

