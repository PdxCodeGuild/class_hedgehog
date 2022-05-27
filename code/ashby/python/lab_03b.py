"""
We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

The code below shows how to loop through an array, and prints the elements one at a time.
"""
import string
#Version 1
"""
#Number list pre-made

nums = [5, 0, 8, 3, 4, 1, 6]

#Essentially recreating this:
#print(sum(nums)/len(nums))

#running total

average = 0

#iterate through list of nums
for num in nums:
    
    #add each number to running total
    
    average += num

#divide total by number of items in list

average /= len(nums)

#print statement

print(f"The average is {average}")

"""



#Version 2

"""
Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.
"""
nums = []
average = 0
#Loop for user input
while True:
    user_input = input("Please enter a number, or 'done' to find the average of all entered valued: ")
    if user_input == "done":
        print("Please give us a moment to tally up your average.")
        break
    #Add user input to list
    nums.append(int(user_input))
#running total
for num in nums:
    average +=num
#exception for zero average / cannot divide by zero error
if average >0:
    average /= len(nums)
print( f"The average of your numbers is {average}!")
