nums = [5, 0, 8, 3, 4, 1, 6]

for num in nums:
    total = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] 
    ave_num = total/len(nums)
print(ave_num)

total = 0

for i in range(len(nums)):
    total = nums[i] + total
    ave_num = total/len(nums)
print(ave_num)


