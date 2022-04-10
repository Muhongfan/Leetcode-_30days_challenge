"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""

"""
recursion
decide the base cases first

"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1], [1, 1]]
        if rowIndex == 0:
            return ans[0]
        elif rowIndex == 1:
            return ans[1]
        else:
            for i in range(2, rowIndex + 1):
                # row = [1 for _ in range(i + 1)]
                ans.append([1] * (i + 1))
                for j in range(1, i):
                    ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
                    #row[j] = ans[i - 1][j - 1] + ans[i - 1][j]
                # ans.append(row)

        return ans[-1]







