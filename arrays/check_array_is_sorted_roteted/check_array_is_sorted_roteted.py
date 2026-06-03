class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums) - 1
        count = 0
        if nums[0] < nums[-1]:
            count += 1
        for i in range(n):
            if nums[i] > nums[i + 1]:
                count += 1
        if count > 1:
            return False

        return True

# nums = [3,4,5,1,2]
nums = [2,1,3,4]
obj= Solution()
print(obj.check(nums))