# lab06b
# credit card validation
# Leigh Fair-Smiley
# 5/31/2022

def validation(sum_num, check_digit):
    if sum_num == check_digit:
        print("Valid!")
        return True
    print("Not valid!")
    return False

def main():
    nums = []
    while True:
        user_input = input("input a number or type 'done' to quit: ")
        if user_input == "done":
            break
        nums.append(int(user_input))
    
    check_digit = nums.pop(len(nums) - 1)
    nums.reverse()
    for x in range(0, len(nums), 2):
        nums[x] *= 2
    for x in range(0, len(nums)):
        if nums[x] > 9:
            nums[x] -= 9
    nums_sum = sum(nums)
    validation(int(str(nums_sum)[1]), check_digit)

main()