nums = input().split()
max = min = float(nums[0])
sum = 0
for i in range(len(nums)):
    sum += float(nums[i])
    if float(nums[i]) > max:
        max = float(nums[i])
    if float(nums[i]) < min:
        min = float(nums[i])
ave = sum / len(nums)
print("最大值为%d,最小值为%d，和为%d，平均值为%.2f" %(max, min, sum, ave))