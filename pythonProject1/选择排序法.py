n = int(input())
nums = input().split()
max = min = int(nums[0])
for i in range(n):
    for x in range(n):
        if int(nums[x]) > max:
            max = int(nums[x])
        if int(nums[x]) < min:
            min = int(nums[x])
print(max,min)