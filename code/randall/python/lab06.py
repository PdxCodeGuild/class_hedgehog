"""
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

1. Convert the input string into a list of ints
2. Slice off the last digit. That is the check digit.
3. Reverse the digits.
4. Double every other element in the reversed list.
5. Subtract nine from numbers over nine.
5. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

1. 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
2. 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
3. 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
4. 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
5. 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
6. 85
7. 5
8. Valid!
"""

def card_validator(cc_num):
    card_list = list(cc_num)
    num_list = []

    for n in card_list:
        num_list.append(int(n))

    check_dig = num_list[-1]
    #print(check_dig)
    num_list.pop()
    num_list.reverse()
    list_doubled = [num_list[n] * 2 if n % 2 == 0 else num_list[n] for n in range(len(num_list))]
    list_sub_nine = [n - 9 if n > 9 else n for n in list_doubled]
    sum_list = sum(list_sub_nine)
    list_sum_list = list(str(sum_list))

    if int(list_sum_list[1]) == check_dig:

        return 'Valid Card Number'
    else:
        return 'Invalid Card Number'
print(card_validator('4556737586899855'))