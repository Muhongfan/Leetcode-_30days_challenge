"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
Accepted
222,926
Submissions
249,137
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #answer = [0]
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

So = Solution()
print(So.runningSum([1,2,3,4]))


def runningSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    running_sum = [nums[0]] if nums else []
    for num_idx, num in enumerate(nums[1:], 1):
        running_sum.append(sum([running_sum[num_idx - 1], num]))

    return running_sum


def runningSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    new = []
    val = 0
    for i in nums:
        val = val + i
        new.append(val)
    return new