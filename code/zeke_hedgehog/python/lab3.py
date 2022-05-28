"""
Lab 3: Average Numbers
We're going to average a list of numbers. 
Start with the following list, iterate through it,keeping a 
'running sum', 
then divide that sum by the 
number of elements 
in that list.
Remember len will give you the length of a list.

The code below shows how to loop through an array, and prints the elements one at a time.

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])
"""

# adding a group of numbers 
# and then dividing by the count of those numbers

""" Version 1 """
# nums = [5, 0, 8, 3, 4, 1, 6]
# running_sum = 0

# for numbers in nums:
#     # print(numbers)
#     # print(len(nums))
#     running_sum = numbers + running_sum
#     # print(total)
# average = running_sum/len(nums) 
# print(average)

#______________________________________________#



#______________________________________________#

"""
Version 2
Ask the user to enter the numbers one at a time, 
putting them into a list.

If the user enters 'done',
then calculate and display the average.
The following code demonstrates how to add an element 
to the end of a list.

nums = []
nums.append(5)
print(nums)
Below is an example input/output:

> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4
"""


# def average_list():
#     for numbers in nums:
#      running_sum = numbers + running_sum
# print(total)
# average = running_sum/len(nums) 
# print(average)


#________________________

# adding a group of numbers 
# and then dividing by the count of those numbers

list = []
running_sum = 0

while True:
    nums = input("enter a number, or 'done': ")
    if nums == 'done':
        break
    else:list.append(int(nums))

print(list)
for item in list:
    running_sum += item 
    average = running_sum/len(list)

print(average)
#----------------------------------
