# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

# Convert the input string into a list of ints


def main():

    user_input = list(input("Enter your credit card number: "))
    num_list = []

    for x in user_input:
        num_list.append(int(x))


    # Slice off the last digit. That is the check digit.
    check = (num_list[:-1])
    check_list = check

    # Reverse the digits.
    check_list.reverse()

    # Double every other element in the reversed list.
    dub = [x * 2 if user_input % 2 == 0 else x for user_input, x in enumerate(check_list)]

    # subtract nine from numbers over nine.
    sub_list = [x - 9 if x > 9 else x for x in dub]
            
    # Sum all values.
    add_all = sum(sub_list)

    # Take the second digit of that sum.
    add_all = int(str(add_all)[:-1])

# If that matches the check digit, the whole card number is valid.
    if add_all == check[-1]:
        print(f"valid {add_all} is = {check[-1]}")
    else:
        print(f"Not valid {add_all} is != {check[-1]}")

main()

            
   