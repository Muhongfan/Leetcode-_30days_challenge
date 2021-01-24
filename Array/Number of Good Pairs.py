"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

"""
import collections


def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    answer = []
    count = collections.Counter(nums)
    for num in count:
        if count[num] > 1:
            answer.append(mulcul(count[num]-1))
    return sum(answer)


def mulcul(n):
    if n == 1:
        return 1
    else:
        return n+(mulcul(n-1))

print(numIdenticalPairs([1,1,1,1]))
