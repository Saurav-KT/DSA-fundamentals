'''
Given a sorted array, arr[] and a number target, you need to find the
number of occurrences of target in arr[].

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.
'''

def count_freq( arr, target):
    # code here
    first = find_first_occurrence(arr, target)
    if first == -1:
        return 0
    second = find_last_occurrence(arr, target)
    result = (second - first) + 1
    return result

def find_first_occurrence(nums, target):
    low, high=0,len(nums)-1
    first=-1
    while low<= high:
        mid= (low+high)//2
        if nums[mid]== target:
            first= mid
            high= mid-1
        elif nums[mid]< target:
            low= mid+1
        else:
            high= mid-1
    return first

def find_last_occurrence(nums, target):
    low, high = 0, len(nums) - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid]== target:
            last= mid
            low= mid+1
        elif nums[mid]< target:
            low= mid+1
        else:
            high= mid-1
    return last