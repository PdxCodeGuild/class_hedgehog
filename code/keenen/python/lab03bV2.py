nums = []

while True: 
    user_input = input("Enter a number, or 'done' to quit: ")
    if user_input.lower() == 'done':
        break
    if user_input == int or float:
        nums.append(int() or float(user_input))
        

total = 0
for num in nums:
    total = total + num
avg = total / len(nums)

print(f"The average of the numbers you've provided is: {avg}")
    
        
