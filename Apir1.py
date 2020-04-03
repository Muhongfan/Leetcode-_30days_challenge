"""
SINGLE NUMBER

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
#Solution 1:
class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = nums[0]
        for i in range(1, len(nums)):
            N = N ^ nums[i]
        return N

#Solution 2:
class Solution(object):
    def sn(self, nums):
        n = []
        for i in nums:
            if nums.count(i) == 1:
                n.append(i)

        return n.pop()


