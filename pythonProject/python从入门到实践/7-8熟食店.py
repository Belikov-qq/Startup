#熟食店
sandwich_orders = ["peanut sandwich","fruits sandwich","tomato sandwich"]
finished_sandwiches = []
for one in sandwich_orders:
    finished_sandwiches.append(one)
    print("I had made " + one.title() + "for you!")
print("I have made these sandwiches for you:")
for one in finished_sandwiches:
    print(one)

