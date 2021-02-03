def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the follow things:")
    for topping in toppings:
        print("-" + topping)
