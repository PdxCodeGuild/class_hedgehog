def cc_valid():
    cc_num_input = list(input("Enter your credit card number: "))
    for num in range(0, len(cc_num_input)):
        cc_num_input[num] = int(cc_num_input[num])
    
    check_digit = str(cc_num_input.pop(-1))
    cc_num_input.reverse()
    
    for num in range(0, len(cc_num_input), 2):
       cc_num_input[num] *= 2 
   
    for num in range(0, len(cc_num_input)):
       if cc_num_input[num] > 9:
           cc_num_input[num] -= 9
    
    total = sum(cc_num_input)
    total = str(total)
    
    if total[1] == check_digit:
        print("Valid")
    else: 
        print("Invalid")

cc_valid()