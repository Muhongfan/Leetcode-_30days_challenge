"""

Contiguous Array
Solution
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.


"""

def findMaxLength(nums):
    # print(nums)
    total_sum = 0
    index_map = dict()
    index_map[0] = -1
    res = 0
    for i, num in enumerate(nums):
        if num == 0:
            total_sum -= 1
        else:
            total_sum += 1
        if total_sum in index_map:
            res = max(res, i - index_map[total_sum])
        else:
            index_map[total_sum] = i
    return res

print(findMaxLength([1,1,1,0,0,0,0,1,1,1]))