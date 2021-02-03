a = []
for i in range(2000,3201):
    if i % 7 == 0 and (i % 5 != 0):
        a.append(str(i))
print(','.join(a))
print("\n")

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=",")
print("\n")

print(*(i for i in range(2000,3201)if i % 7 == 0 and i % 5 != 0),sep=',')
print("\n")