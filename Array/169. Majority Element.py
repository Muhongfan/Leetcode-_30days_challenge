"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1

"""

from collections import Counter
# Counter().most_common()
#[(item1, freq1), (item2, freq2)...]
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        most_common, most_freq = Counter(nums).most_common(1)[0]
        return most_common

# exceeding time: only item without freq
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(nums, key=nums.count)
