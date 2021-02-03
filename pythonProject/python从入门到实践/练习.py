for num in range(1,20):
    print(num)

list = range(1,1000000)
print(list)

min(list)
max(list)
summer = sum(list)
print(summer)

for jishu in range(1,20,2):
    print(jishu)

numbers = []
for nums in range(1,30):
    if nums%3 == 0:
        numbers.append(nums)
print(numbers)

squares = []
for i in range(1,10):
    squares.append(i**3)
print(squares)

squares = [i**3 for i in range(1,10)]
print(squares)