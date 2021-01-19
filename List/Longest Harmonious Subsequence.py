"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0


Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
"""
import collections
# find the longest sub list that the difference between maximum and minimum elements is 1
# out of time
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        answer = 0
        #for n in count.keys():
        for n in count:
            if n + 1 in count:
                answer = max(answer, count[n] + count[n+1])
        return answer


so = Solution()
print(so.findLHS([1,3,2,2,5,2,3,7]))


def findLHS2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = collections.Counter(nums)
    return max([count[n]+count[n+1] for n in count if n+1 in count] or [0])
    #return max([count[n]+count[n+1] for n in count if n+1 in count], default=0)