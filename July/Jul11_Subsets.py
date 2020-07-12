"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""


def subsets(nums):
    final = [[]]
    for num in nums:
        final += [item + [num] for item in final]
    return final

def subsets2(nums):
    final = []
    def dfs(path, index):
        final.append(path)
        for i in range(index, len(nums)):
            dfs(path + [nums[i]], i + 1)
    dfs([], 0)
    return final

