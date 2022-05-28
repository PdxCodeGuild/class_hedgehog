# lab03b
# Average num
# Leigh Fair-Smiley
# 5/26/2022

nums = []
while True:
    user_input = input("Enter a number or 'done': ")
    if user_input == "done":
        break
    nums.append(int(user_input))

total = 0
for num in nums:
    total += num
    
print(f"average: {int(total / len(nums))}")
