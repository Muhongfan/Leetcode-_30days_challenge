"""
1365. How Many Numbers Are Smaller Than the Current Number
Easy

1346

32

Add to List

Share
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.



Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]


Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
"""

#暴力
import collections


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] > nums[j]:
                        count += 1
            answer.append(count)
            count = 0

        return answer

# Constraints:
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

# def smallerNumbersThanCurrent(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     #count = 0
#     num_list = sorted(nums)
#     counts = collections.Counter(num_list)
#     return [counts[num] for num in nums]
#



def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    indices = {}
    for id, num in enumerate(sorted(nums)):
        indices.setdefault(num, id)
    return [indices[x] for x in nums]

print(smallerNumbersThanCurrent([8,1,2,2,3]))


