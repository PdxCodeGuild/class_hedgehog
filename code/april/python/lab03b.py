
"""
Lab 3: Average Numbers
April 
26 May 2022
"""
"""
###### Version 1 #####

We're going to average a list of numbers. Start with the following list, 
iterate through it, keeping a 'running sum', then divide that sum by the 
number of elements in that list. Remember len will give you the length of 
a list.
"""

nums = [5, 0, 8, 3, 4, 1, 6]

sum_nums = 0

for num in nums: # iterate through list
    sum_nums += num # get running sum
    average = sum_nums/len(nums) # get average by dividing sum by number of elements in list

# print nums, sum, and average
print(f"Nums: {nums}\nSum: {sum_nums}\nAverage: {round(average)}")

"""
###### Version 2 #####

Ask the user to enter the numbers one at a time, 
putting them into a list. If the user enters 'done', 
then calculate and display the average. 
"""

nums = []
sum_nums = 0

while True:
    number = input("Enter a number or enter 'done' when finished: ") # prompt for user input
    if number == 'done': # stop when user enters 'done'
        break
    nums.append(int(number)) # add to list
for num in nums: # iterate through list
    sum_nums += num # get running sum
    average = sum_nums/len(nums) # get average by dividing sum by number of elements in list    

print(f"You entered: {nums}\nThe sum is {sum_nums}\nThe average is: {round(average)}") #print list, sum, and average