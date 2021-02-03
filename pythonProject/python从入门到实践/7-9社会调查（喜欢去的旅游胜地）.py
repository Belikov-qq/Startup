responsers = {}
survey = True
while survey:
    ask = input("Would you help me to do a survey?(yes or no):")
    if ask == 'yes':
        name = input("\nHello!What's your name?:")
        response = input("\nWhat's the places you want to go to the most?")
        responsers[name] = response
    elif ask == 'no':
        survey = False
    else:
        print("\nPlease input correct anwsers!")
print('\n------Result------')
for name,response in responsers.items():
    print(name + " want to go to " + response + ".")