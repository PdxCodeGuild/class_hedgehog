# Lab 3: Average Numbers
# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

'''nums = [5, 0, 8, 3, 4, 1, 6]
sum = 0
average = 0
for num in nums:
    sum += num
average = sum / len(nums)
print(average) #check work
'''

###################################################################################
# Version 2
# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.
nums = []
sum = 0
average = 0
while True:
    num = input("Enter a number to suma nd average or 'done' to quit: \n\t> ").lower().replace(' ','')
    if num == 'done':
        break
    elif num.isnumeric():
        nums.append(int(num))
    else:
        print("That was not a valid option.")
for num in nums:
    sum += num
average = sum / len(nums)
if sum % len(nums) == 0:
    average = int(average)
print(f"The numbers you entered are: {nums}\nThe sum is: {sum}\nThe average is: {average}")
