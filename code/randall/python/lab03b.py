#==========
#Version 1:
#==========
#We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then #divide that sum by the number of elements in that list. Remember len will give you the length of a list.

numbers = [5, 0, 4, 3, 4, 1, 5]
length = len(numbers)
total = 0
sum_total = 0
for number in numbers:
    total += numbers[sum_total]
    sum_total += 1
average = total / sum_total
print(f"Average for the list of numbers provided is: {average}")

"""
#==========
#Version 2:
#==========
#Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and #display the average.

numbers = []

while True:
    user_num = input("Enter multiple numbers then type 'done' when finished: ")
    
    if user_num != 'done':
        numbers.append(int(user_num))
    else:
        add_num = len(numbers)
        
        total = 0
         
        start_val = 0

        for i in numbers:
            total += numbers[start_val]
            
            start_val += 1
        
        average = total/add_num
        print(f"Average for the numbers provided is: {average}")
        """