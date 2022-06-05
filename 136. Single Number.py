"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""
from collections import Counter, defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for value, nums in Counter(nums).items():
            if nums == 1:
                return value

    def singleNumber(self, nums):
        hashtable = defaultdict(int)
        for i in nums:
            hashtable[i]+=1
        for i in hashtable:
            if hashtable[i] ==1:
                return i
