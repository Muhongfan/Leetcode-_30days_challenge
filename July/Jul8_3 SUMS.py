"""

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(0, len(nums)):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue  #
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.append((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                    while(nums[j] == nums[j - 1] and nums[k] == nums[k + 1] and j < k):
                        j += 1
                elif sum > 0:
                    k -= 1
                    while(nums[k] == nums[k + 1] and j < k):
                        k -= 1
                else:
                    j += 1
                    while(nums[j] == nums[j - 1] and j < k):
                        j += 1
        return list(set(result))