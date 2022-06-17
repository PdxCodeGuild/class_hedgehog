def main():
    list_of_nums = []
    user = input('Enter a 16 digit number or "done" to quit: ')
    # print(user)

    if user != 'done':
        for x in user:
            # print(f'the value is {x}')
            list_of_nums.append(int(x))
            

    # print('list of nums ', list_of_nums)

    check_digit = list_of_nums.pop()
        
    # print('check digit ', check_digit)

    # print('list of nums minus check ', list_of_nums)
    
    sliced_nums = list_of_nums

    # print(sliced_nums)
    
    sliced_nums.reverse()

    # print('reversed ', sliced_nums)

    for index, value in enumerate(sliced_nums):
        # print(f'index: {index}, value: {value}')
        if index % 2 == 0:
            # print(index)
            sliced_nums[index] = value *2 
        
            # print(f'double: {doubled_value}')
    # print(sliced_nums)

    sub_9 = []

    for value in sliced_nums:
        if value > 9:
            # print(value)
            value -= 9
            sub_9.append(value)
            # print(value)
        else:
            sub_9.append(value)

    # print('list of subtract nine: ', sub_9)

    total = sum(sub_9)
    # print(total)

    result = total % 10

    # print(result)

    if result == check_digit:
        print('Valid!')             
    else:
        print('Invalid!')   

main()