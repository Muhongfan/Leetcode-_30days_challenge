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
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = []
        for i in range(rowIndex +1):
            answer.append([])
            for j in range(i+1):
                if j ==0 or j == i:
                    answer[i].append(1)
                else:
                    answer[i].append(answer[i-1][j-1]+ answer[i-1][j])
        return answer
