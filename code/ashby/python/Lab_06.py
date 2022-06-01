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

def credit_card_check(card_num = str):
# Slice off the last digit. That is the check digit.
#Convert the input string into a list of ints
    card_list_int = []
    card_list_str = list(card_num)
    total_check=0
    check_value = int(card_list_str.pop())
    print(check_value)
    print(card_list_str)
    for num in card_list_str:
        card_list_int.append(int(num))
    print(card_list_int)
    # Reverse the digits.
    card_list_int.reverse()
    print(card_list_int)
    print(len(card_list_int))
    # Double every other element in the reversed list.
    for x in range(0,len(card_list_int),2):
        card_list_int[x] *=2
    print(card_list_int)
    # Subtract nine from numbers over nine.
    for x in range(len(card_list_int)):
        if card_list_int[x] > 9:
            card_list_int[x] -= 9
            # Sum all values.
        total_check += card_list_int[x]
    print(card_list_int)
    print(total_check%10)
    # If that matches the check digit, the whole card number is valid.
    if total_check%10 == check_value:
        print("Valid!")
        return True
    else:
        print("Invalid!")
        return False        


print(credit_card_check(123456789))