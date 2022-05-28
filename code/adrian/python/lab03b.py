
# We're going to average a list of numbers. 
# Start with the following list, iterate through it, 
# keeping a 'running sum', then divide that sum by the number of elements in that list. 
# Remember len will give you the length of a list.


# Version 1

nums = [5, 0, 8, 3, 4, 1, 6]
result = []
i = 0

# loop over the elements
for num in nums:
    i += num
    result.append(i)

print(i / len(nums))

