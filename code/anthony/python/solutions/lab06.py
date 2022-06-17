
from tkinter import E


def is_valid():
    card_num = input("Enter your card number: ")
    # Convert the input string into a list of ints
    # ex: 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
    cc_num = []
    card_num = card_num.split()
    for num in card_num:
        cc_num.append(int(num))

    # Slice off the last digit. That is the check digit.
    check_digit = cc_num.pop()

    # Reverse the digits.
    cc_num.reverse()

    # Double every other element in the reversed list.
    counter = 0
    for num in cc_num:
        if counter % 2:
            pass
        else:
            cc_num[counter] = num * 2

        # Subtract nine from numbers over nine.
        if cc_num[counter] > 9:
            cc_num[counter] -= 9
        counter += 1

    # Sum all values.
    total = sum(cc_num)

    # Take the second digit of that sum.
    check = int(str(total)[1])

    # If that matches the check digit, the whole card number is valid.
    return check == check_digit


print(is_valid())
