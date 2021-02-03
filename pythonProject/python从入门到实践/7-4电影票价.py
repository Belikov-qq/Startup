#电影票价
active = True
while active:
    prompt = "I can help you about the correct price of the ticket."
    prompt += "\nPlease write down your age:(You could write 'quit' to quit)"
    age = input(prompt)
    if age != "quit":
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
    else:
        active = False