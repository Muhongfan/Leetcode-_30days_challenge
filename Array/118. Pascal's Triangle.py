"""
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<2:
            return [[1]]
        nums = [[1],[1,1]]
        for i in range(2,numRows):
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1,i):
                row[j] = nums[i-1][j-1]+nums[i-1][j]
            nums.append(row)
        return nums