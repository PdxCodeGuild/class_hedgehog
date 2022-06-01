"""
Lab 6: Credit Card Validation
April
31 May 2022
"""

#sample_cc = 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5

def main():
    # Take credit card number as input 
    credit_card_number = (input("Enter the credit card number: \n"))   

    # Convert the input string into a list of ints
    cc_convert = credit_card_number.split() 

    cc_list = []
    for nums in cc_convert:
        cc_list.append(int(nums))
    print(f"Credit card number as list: \n{cc_list}")

    # Slice off the last digit. That is the check digit.
    check_digit = cc_convert[-1] # Use later for validation
    print(f"The check digit is: \n{check_digit}")

    del cc_list[-1] # Use del to remove last digit from list
    print(f"List with last digit sliced off: \n{cc_list}")

    # Reverse the digits.
    cc_list.reverse()
    print(f"List reversed: \n{cc_list}")

    # Double every other element in the reversed list.
    for numbers in range(0, len(cc_list), 2): # For numbers between 0 and length of cc_list, in increments of 2
        cc_list[numbers] *= 2 # Multiply every other digit by 2
    print(f"Every other element doubled: \n{cc_list}")    

    # Subtract nine from numbers over nine.
    for numbers in range(len(cc_list)):
        if cc_list[numbers] > 9: # If a number in list is over 9, subtract 9
            cc_list[numbers] -= 9
    print(f"Numbers over 9 with 9 subtracted: \n{cc_list}")    

    # Sum all values.
    sum_all = sum(cc_list)
    print(f"Sum of all values: \n{sum_all}")
    
    # Take the second digit of that sum.
    sum_check = str(sum_all)[1]

    # If that matches the check digit, the whole card number is valid.  
    if sum_check == check_digit: # If second digit of sum = check_digit card number is valid
        print("Card is valid")
        return True
    else:
        print("Card is not valid") # If not, not valid
        return False

main()    