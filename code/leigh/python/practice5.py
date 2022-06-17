

# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"




# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def even_even(nums):
    total_even = 0
    for num in nums:
        if not num % 2:
            total_even += 1
    return not total_even % 2

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
    combined = []
    for i in range(len(nums1)):
        combined.append(nums1[i])
        combined.append(nums2[i])
    return combined
    
def test_combine():
    assert combine(['a','b','c'],[1,2,3]) == ['a', 1, 'b', 2, 'c', 3]



# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.


def find_pair(nums, target):
    pair = []
    found_pair = False
    for i in range(len(nums)):
        for x in range(len(nums)):
            if i != x:
                if nums[i] + nums[x] == target:
                    print("totaled 7")
                    pair.append(nums[i])
                    pair.append(nums[x])
                    found_pair = True
                    break
        if found_pair:
            break
    return pair

def test_find_pair():
    assert find_pair([5, 6, 2, 3], 7) == [5, 2]




# Average
# Write a function to find the average of a list of numbers


def average(nums):
    return sum(nums) / len(nums)

def test_average():
    assert average([1, 2, 3, 4, 5]) == 3


# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    for i, string in enumerate(mylist):
        if not string:
            mylist.pop(i)
    return mylist

def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']



# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    merges = []
    for i in range(len(nums1)):
        merge = []
        merge.append(nums1[i])
        merge.append(nums2[i])
        merges.append(merge)
    return merges
    
def test_merge():
    assert merge([5,2,1], [6,8,2]) == [[5,6],[2,8],[1,2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.


def combine_all(nums):
    combined = []
    for list in nums:
        for num in list:
            combined.append(num)
    return combined
    
def test_combine_all():
    assert combine_all([[5,2,3],[4,5,1],[7,6,3]]) == [5,2,3,4,5,1,7,6,3]

