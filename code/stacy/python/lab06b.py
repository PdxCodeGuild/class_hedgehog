def credit_card_number_checker():
    credit_card_number_string = input("Please enter your credit card number: \n\t> ").replace(' ','')
    cc_nums = []
    print(type(cc_nums))
    for num in credit_card_number_string:
        cc_nums.append(int(num))
    check_digit = str(cc_nums.pop())
    cc_nums.reverse()
    for num in cc_nums:
        if cc_nums[num] %2 == 0:
            num *= 2
    for num in cc_nums:
        if num >= 9:
            num-= 9
    sum = 0
    for num in cc_nums:
        sum+= num
    sum = str(sum)
    if check_digit == sum[1]:
        return True
    else:
        return False

print(credit_card_number_checker())


'''
Lab 6: Credit Card Validation
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''