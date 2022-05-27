#########------VERSION 1---------##########
# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', 
# then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

# The code below shows how to loop through an array, and prints the elements one at a time.

nums = [5, 0, 8, 3, 4, 1, 6]
sum = 0
for i in range(0, len(nums)):

    sum = sum + nums[i]
    average = sum / 2

print(average)
# loop over the elements
# for num in nums:
#     print(sum(nums))

# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])
#     sum = nums[i] + num[i]
#     print(sum)

# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.
sum = 0
nums = []

while True:
    user_num = input("Enter a number or 'done' to quit: ")
    
    if user_num == 'done':
        
        for i in range(0, len(nums)):
            sum = sum + nums[i]
            average = sum / 2

        print(f"The sum of you list is{sum} and the average is {average}.")
        break
    else: 
        user_num = int(user_num)
        
        nums.append(user_num)

