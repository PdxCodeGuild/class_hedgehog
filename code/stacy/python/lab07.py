def peaks(dataset):
    peak_indices = []
    for x in range(1, len(dataset)-1):
        if dataset[x] > dataset[x+1] and dataset[x] > dataset[x-1]:
            peak_indices.append(x)
    return peak_indices
    
def valleys(dataset):
    valley_indices = []
    for x in range(1, len(dataset)-1):
        if dataset[x] < dataset[x+1] and dataset[x] < dataset[x-1]:
            valley_indices.append(x)
    return valley_indices
        
def peaks_and_valleys(dataset):
    peak_valley_indices = []
    peak_indices = peaks(dataset)
    valley_indices = valleys(dataset)
    for x in range(len(peak_indices)):
        peak_valley_indices.append(peak_indices[x])
        peak_valley_indices.append(valley_indices[x])
    return peak_valley_indices

def is_an_x_mkI(dataset): #Will print with lines with square brackets on both ends
    visualization_of_data = []
    sorted_dataset = []
    sorted_dataset.extend(dataset)
    num_of_lines = sorted_dataset.pop()
    index = 0
    for line in range(num_of_lines):
        visualization_of_data.append([])
        index += 1
    index = 0
    for line in range(num_of_lines):
        for num in dataset:
            if num >= line+1:
                visualization_of_data[index].append('x')
            else:
                visualization_of_data[index].append(' ')
        index += 1
    visualization_of_data.reverse()
    visualization_of_data_string = ''
    for line in visualization_of_data:
        visualization_of_data_string += ''.join(line)+'\n'
    return visualization_of_data_string

def main():    
    dataset = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
    visualization = is_an_x_mkI(dataset)
    print(visualization)
main()


''' Version 3'''

# def is_an_x_mkI(dataset): #Will print with lines with square brackets on both ends
#     visualization_of_data = []
#     sorted_dataset = []
#     sorted_dataset.extend(dataset)
#     num_of_lines = sorted_dataset.pop()
#     index = 0
#     for line in range(num_of_lines):
#         visualization_of_data.append([])
#         index += 1
#     index = 0
#     index2 = 0
#     peak_indices = peaks(dataset)
#     for line in range(num_of_lines):
#         for num in dataset:
#             if num >= line+1:
#                 visualization_of_data[index].append('x')
#             # elif num <= peak_indices[index2]:
#             #     visualization_of_data[index].append('o')
#             #     index2 += 1
#             else:
#                 visualization_of_data[index].append(' ')
#         index += 1
#     visualization_of_data.reverse()
#     visualization_of_data_string = ''
#     for line in visualization_of_data:
#         visualization_of_data_string += ''.join(line)+'\n'
#     return visualization_of_data_string


'''
Peaks and Valleys
Define the following functions:

peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

Visualization of test data:

Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
POI							P			V					P			V			
Example I/O:

                                                  X                 X
                                               X  X  X           X  X
                          X                 X  X  X  X  X     X  X  X
                       X  X  X           X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# index 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks(data) # [6, 14]
valleys(data) # [9, 17]
peaks_and_valleys(data) # [6, 9, 14, 17]
Version 2 (optional)
Using the data list above, draw the image of X's above.

Hint 1: If you wanted to draw this horizontally, you could do so very easily like this.

for num in data:
    print('x' * num)
Hint 2: print can only work on one line at a time, so you'll have to loop and decide to either print a space ' ' or an 'X' for every column.

Version 3 (optional)
Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the water is represented by O's. Given data, calculate the amount of water that would be collected, and if you can, draw the following diagram.

                                                  X  O  O  O  O  O  X
                                               X  X  X  O  O  O  X  X
                          X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
                       X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

'''