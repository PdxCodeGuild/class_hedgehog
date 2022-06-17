


# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"




# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def even_even(nums):
    even = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
    if len(even) % 2 == 0:
        return True
    else:
        return False        

def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False


## Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    nums.reverse()
    return nums


def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]


# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
    common = []
    for num in nums1:
        if num in nums2:
            common.append(num)
    return common          

def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.

def combine(nums1, nums2):
    # use zip to combine the two lists alternating each element
    combined_list = [x for x in zip(nums1, nums2) for x in x]
    return combined_list

def test_combine():
    assert combine(['a','b','c'],[1,2,3]) == ['a', 1, 'b', 2, 'c', 3]

# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers 
# from the list that sum to a target number. 
# Optional: return a list of 
# all pairs of numbers that sum to a target value.

"""Soution 1"""
def find_pair(nums, target):
    pairs = [] 
    while nums: #loop to go through nums
        num = nums.pop() # pop and put in num
        find_pairs = target - num # subtract the popped num from the target
        if find_pairs in nums: # see if that difference is in nums
            pairs = [find_pairs, num] 
    return pairs

"""
Optional Solution for all pairs that sum to target value

Doesn't work is test below, but does work if you put in a 
value like find_pair([5, 6, 2, 3, 4, 1], 7)
"""
# def find_pair(nums, target):
#     pairs = [] 
#     while nums: 
#         num = nums.pop() 
#         find_pairs = target - num 
#         if find_pairs in nums: 
#             pairs.append((find_pairs, num)) # append any pairs found to the pairs list
#     return pairs # returns list containing all pairs of number 


def test_find_pair():
    assert find_pair([5, 6, 2, 3], 7) == [5, 2]


# Average
# Write a function to find the average of a list of numbers

def average(nums):
    average = (sum(nums)) / len(nums)
    return average
   
def test_average():
    assert average([1, 2, 3, 4, 5]) == 3


# Remove Empty
# Write a function to remove all empty strings from a list.

def remove_empty(myList):
    while("" in myList) :
        myList.remove("")

    return myList

def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']



# Merge
# Write a function that merges two lists into a single list, where each 
# element of the output list is a list containing two elements, one from 
# each of the input lists.

"""Solution 1"""
# def merge(nums1, nums2):
#     list = []
#     for num in range(len(nums1)):
#         pairs = []
#         pairs.append(nums1[num])
#         pairs.append(nums2[num])
#         list.append(pairs)
#     return list

"""Solution 2 (condensed)"""
# def merge(nums1, nums2):
#     list = []
#     for num in range(len(nums1)):
#         list.append([nums1[num], nums2[num]])
#     return list

"""Solution 3 (condensed using list comprehension)"""
def merge(nums1, nums2):
    list = [[nums1[num], nums2[num]] for num in range(len(nums1))]
    return list
    
def test_merge():
    assert merge([5,2,1], [6,8,2]) == [[5,6],[2,8],[1,2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list 
# containing each element from each of the lists.

def combine_all(nums):
    all = []
    for num in nums:
        for item in num:
            all.append(item)
    return all      
     
    
def test_combine_all():
    assert combine_all([[5,2,3],[4,5,1],[7,6,3]]) == [5,2,3,4,5,1,7,6,3]




