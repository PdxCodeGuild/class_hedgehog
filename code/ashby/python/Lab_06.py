""" Credit Card Validation"""


card_num = "4556737586899855"

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

def credit_card_check(card_num):
# Slice off the last digit. That is the check digit.
#Convert the input string into a list of ints
    card_list_int = []
    card_list_str = list(card_num)
    total_check=0
    check_value = int(card_list_str.pop())

    for num in card_list_str:
        card_list_int.append(int(num))
    # Reverse the digits.
    card_list_int.reverse()
    # Double every other element in the reversed list.
    for x in range(0,len(card_list_int)):
        if x %2 ==0:
            card_list_int[x] *=2
        if card_list_int[x] > 9:
            card_list_int[x] -=9
        total_check += card_list_int[x]
    # Subtract nine from numbers over nine.
    # If that matches the check digit, the whole card number is valid.
    if total_check%10 == check_value:
        print("Valid!")
        return True
    else:
        print("Invalid!")
        return False        


print(credit_card_check(card_num))