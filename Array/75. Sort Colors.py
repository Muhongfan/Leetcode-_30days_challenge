"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[j], nums[i] = nums[i], nums[j]
        return nums
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = cur = 0
        r = len(nums)-1
        while cur<r:
            if nums[cur] == 0:
                nums[l], nums[cur] = nums[cur], nums[l]
                l +=1
                cur +=1
            elif nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r-=1
            else:
                cur +=1

    def sortColors3(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            cur = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[cur]:
                    cur = j
            if i != cur:
                nums[i], nums[cur] = nums[cur], nums[i]
        return nums
