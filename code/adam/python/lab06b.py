# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!





def valid():
        credit_num = input("Enter a 16 digit credit card number")
        #credit_num = "4556737586899855"
        numbers = []
        credit_num = list(credit_num)
        for num in credit_num:
                numbers.append(int(num))
        #print(numbers) 

       
        check_dig = numbers.pop()
        # print(numbers)
        numbers.reverse()


        # print("numbers", numbers)
        counter = 0
        for num in numbers:
                              
                
                if counter % 2:
                        pass
                else:
                
                      numbers[counter] = num * 2
                      if numbers[counter] > 9:
                              numbers[counter] = numbers[counter] - 9
                counter += 1
        total = sum(numbers) 
        
        if check_dig == total % 10:
                return True
        
        
          
        
        

        print("numbers", numbers)  



        # sec_num = credit_num[::2]
        # for num in sec_num:
        #        num * 2

                

        
       
        return credit_num 


print(valid())