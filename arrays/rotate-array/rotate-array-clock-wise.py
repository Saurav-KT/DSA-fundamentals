class Solution:

    # Helper function to reverse array between two indices
    def reverse(self, nums: list[int], left: int, right: int):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Function to rotate array right by k steps
    def rotate(self, nums, k):
        n= len(nums)
        if n==0 or k==0:
            return nums

        # normalize k if it's larger than n
        k= k %n

        # reverse the entire array
        self.reverse(nums, 0, n-1)

        # reverse the first k elements
        self.reverse(nums,0, k-1)

        #reverse remaining n-k elements

        self.reverse(nums,k, n-1)
        return nums

# if __name__== "__main__":
#     arr= [1,2,3,4,5,6,7]
#     obj= Solution()
#     obj.rotate(nums=arr,k=3)
#     print(arr)


import unittest

class TestRotateArray(unittest.TestCase):
      def setUp(self):
          self.obj= Solution()

      def test_rotate_normal_case(self):
          nums = [1, 2, 3, 4, 5, 6, 7]
          self.obj.rotate(nums=nums, k=3)
          self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

      def test_rotate_k_greater_than_length(self):
          nums = [1, 2, 3]
          self.obj.rotate(nums, 4)
          self.assertEqual(nums, [3, 1, 2])

      def test_rotate_zero_k(self):
          nums= [1,2,3]
          self.obj.rotate(nums, 0)
          self.assertEqual(nums,[1,2,3])

      def test_empty_array(self):
          nums=[]
          self.obj.rotate(nums,2)
          self.assertEqual(nums, [])

      def test_single_element(self):
          nums=[10]
          self.obj.rotate(nums, 5)
          self.assertEqual(nums, [10])

if __name__ == "__main__":
    unittest.main()





