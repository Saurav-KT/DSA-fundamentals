# Find First and Last Position of element in sorted array
# Input: nums = [5,7,7,8,8,10], target = 8
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

# Linear search time complexity o(n)

def find_range(nums, target):
    first, last= -1,-1
    for i in range(len(nums)):
        if nums[i] == target:
            if first<0:
               first= i
            last= i
    return [first, last]


# binary search o(log n)
def find_first_last_element(nums, target):
    first= find_first_occurrence(nums, target)
    if first ==-1:
        return [-1,-1]
    last= find_last_occurrence(nums, target)
    return [first, last]

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





nums = [5, 7, 7, 8, 8, 10]
print(find_first_last_element(nums, 10))
