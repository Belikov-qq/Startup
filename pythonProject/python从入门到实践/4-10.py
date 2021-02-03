list = ["apple","banana","cheese"]
print("The first three items in the list are:")
for i in list[:3]:
    print(i.title())

pizzas = list[:]
pizzas.append("fruit")
list.append("watermellon")
print("My list is:")
for i in list[:]:
    print(i.title())

print("My pizza is")
for i in pizzas[:]:
    print(i.title())
