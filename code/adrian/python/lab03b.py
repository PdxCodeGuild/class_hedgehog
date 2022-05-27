
# We're going to average a list of numbers. 
# Start with the following list, iterate through it, 
# keeping a 'running sum', then divide that sum by the number of elements in that list. 
# Remember len will give you the length of a list.


# Version 1

# nums = [5, 0, 8, 3, 4, 1, 6]
# result = []
# i = 0

# # loop over the elements
# for num in nums:
#     i += num
#     result.append(i)

# print(i / len(nums))






# Ask the user to enter the numbers one at a time, putting them into a list. 
# If the user enters 'done', then calculate and display the average. 


# Version 2

def sum(nums):
    "Get the sum of the list"
    result = 0
    for num in nums:
        result += int(num)
    return result


nums = []
while True:
    user_number = input("\n Enter a number or 'done' to quit: ")
    if user_number == 'done':
        print(f"You entered: {nums}")
        break
    nums = nums + list(user_number)


print(sum(nums))




