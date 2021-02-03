name = input("Which car do you want to buy?:" )
print("Let me see if I can find you a " + name)


number = input("How many people are you?:")
number = int(number)
if number >= 8:
    print("Sorry, there aren't any other seats!")
else:
    print("Yes,you can have a table!")



shuzi = input("Please input a number:")
shuzi = int(number)
if shuzi % 10 == 0:
    print("This is a correct number!")
else:
    print("Sorry,it's not a correct number!")


