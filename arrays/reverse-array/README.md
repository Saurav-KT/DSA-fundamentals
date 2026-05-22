## Problem: Reverse an Array

###
You are given an array of integers arr[]. You have to reverse the given array.

Note: Modify the array in place.
Examples:

Input: arr = [1, 4, 3, 2, 6, 5]

Output: [5, 6, 2, 3, 4, 1]

Explanation: The elements of the array are [1, 4, 3, 2, 6, 5]. 
After reversing the array, the first element goes to the last position, 
the second element goes to the second last position and so on. Hence,
the answer is [5, 6, 2, 3, 4, 1].

###

###

Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are [4, 5, 2]. The reversed array will be [2, 5, 4].

###

###
Input: arr = [1]
Output: [1]
Explanation: The array has only single element, hence the reversed array is same as the original.

###

### Implementation
Right Rotation (or Clockwise)
Instead of simulating each rotation one by one, we can get the rotated array in-place by reversing specific parts of the array. This works because rotating is just rearranging sections of the array.

For Right Rotation by k steps:
Reverse the entire array
Reverse the first k elements
Reverse the remaining n - k elements

Normalize k by doing k = k % N

If direction is "right":
Reverse the entire array
Reverse the first k elements
Reverse the rest (from k to end)

###