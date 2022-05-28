nums = []

total = 0

while True:

    user_num = input("Please enter a number or 'done' to find the average: ")

    if user_num == "done":
        for i in range(len(nums)):
         total = nums[i] + total
         ave_num = total/len(nums)
        print(f"{ave_num} is your average")
        break
        
    nums.append(int(user_num))
