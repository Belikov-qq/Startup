n = int(input())
nums = input().split()
for i in range(n):
    for x in range(n-1):
        if int(nums[x]) > int(nums[x+1]):
            nums[x], nums[x+1] = nums[x+1], nums[x]
print(nums)
