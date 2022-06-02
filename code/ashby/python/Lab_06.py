""" Credit Card Validation"""


from typing import Type


card_num = "4556737586899855"

def credit_card_check(card_num:str):
    card_list_int = []
    try:
    
        card_list_str = list(card_num)
    except TypeError:
        return "Invalid input. This function only supports a string input."
    total_check=0

    # Slice off the last digit. That is the check digit.
    check_value = int(card_list_str.pop())

    #Convert the input string into a list of ints
    for num in card_list_str:
        card_list_int.append(int(num))

    # Reverse the digits.
    card_list_int.reverse()

    # Double every other element in the reversed list.
    for x in range(0,len(card_list_int)):
        if x %2 ==0:
            card_list_int[x] *=2

    # Subtract nine from numbers over nine.
        if card_list_int[x] > 9:
            card_list_int[x] -=9
        total_check += card_list_int[x]

    # Take the second digit of that sum.
    # If that matches the check digit, the whole card number is valid.
    if total_check%10 == check_value:
        print("Valid!")
        return True
    else:
        print("Invalid!")
        return False        


print(credit_card_check(card_num))


print(credit_card_check(["4","5","5",6,7,3,7,5,8,6,8,9,9,8,5,5]))