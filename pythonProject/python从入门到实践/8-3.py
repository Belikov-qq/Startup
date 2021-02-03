def make_shirt(size,content):
    print("The size of T-shirt is " + size + ".")
    print("The contents are: " +content + ".")

make_shirt('XL','Mysery')


def make_loveshirt(size,content='I love Python.'):
    print("The size of the T-shirt is " + size + ".")
    print("The contents are:" + content )
make_loveshirt('XL')

def describe_city(name,country):
    print(name + " is in " + country + ",it's a beautiful city.")
describe_city('Shanghai','China')