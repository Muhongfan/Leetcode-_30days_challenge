"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
from collections import Counter


def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    nums = Counter(nums)
    return [k for k, v in nums.items() if v == 2]
print(findDuplicates([4,3,2,7,8,2,3,1]))