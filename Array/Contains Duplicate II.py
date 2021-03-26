"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

"""

"""
遍历所有元素，将元素值当做键、元素下标当做值，存放在一个字典中。
遍历的时候，如果发现重复元素，则比较其下标的差值是否小于k，
如果小于则可直接返回True，否则更新字典中该键的值为新的下标。
"""
def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    num_map = {}
    for i in xrange(len(nums)):
        if nums[i] in num_map and i - num_map[nums[i]] <= k:
            return True
        else:
            num_map[nums[i]] = i
    return False

"""
在遍历列表的时候维护一个集合，集合中保存当前元素前面的k个元素，每次访问一个元素时判断是否在该集合中出现过。

"""
def containsNearbyDuplicate2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    window = set([])
    for i in xrange(len(nums)):
        if i > k:
            window.discard(nums[i - k - 1])
        if nums[i] in window:
            return True
        else:
            window.add(nums[i])
    return False
