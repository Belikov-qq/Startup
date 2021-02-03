#比萨配料
active = True
prompt = "What things do you want to add in you pizza?"
prompt += "\nPlease write down:"
while active:
    name = input(prompt)
    if name != "quit":
        print("OK,I'll add " + name + "to your pizza!")
    else:
        active = False


