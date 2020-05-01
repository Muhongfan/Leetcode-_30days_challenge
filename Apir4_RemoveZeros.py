"""
Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

# Solution1:

def moveZeroes( nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zeros = 0
    for i in nums:
        if i != 0:
            nums[zeros] = i
            zeros += 1
    # nums = list(nums + [0] * zeros)
    # print(li)
    for j in range(zeros, len(nums)):
        nums[j] = 0
    return nums

print(moveZeroes([0,0,1]))


# Solution2:
def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # O(N) and O(1)
    #         zero_index = 0
    #         for i in range(len(nums)):
    #             if nums[i] != 0:
    #                 nums[zero_index] = nums[i]
    #                 zero_index += 1

    #         #hit the end of array
    #         #now to populate zeros

    #         for i in range(zero_index, len(nums)):
    #             nums[i] = 0
    nonzero = 0
    for i, val in enumerate(nums):
        if val != 0:
            nums[nonzero], nums[i] = nums[i], nums[nonzero]
            nonzero += 1
    return nums

# Solution 3
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    nums.sort(key=lambda x: 1 if x == 0 else 0)
    return nums
"""
def getKey(x):
    if x == 0:
        return 1
    else:
        return 0
"""