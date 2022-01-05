"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
class Solution:
    def moveZeroes(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = sorted(nums)
        count = 0
        for i in nums:
            if i == 0:
                count+=1
            elif i!=0:
                break
        nums[:] = nums[count:] + nums[:count]
        return nums

    def moveZeros2(self, nums):
        slow = 0
        fast = 1
        length = len(nums) - 1

        while slow <= length and fast <= length:
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow] = nums[fast]
            nums[fast] = 0

        if nums[slow] != 0:
            slow += 1

        fast += 1

        return nums


anser = Solution()
print(anser.moveZeroes([0,1,0,3,12]))