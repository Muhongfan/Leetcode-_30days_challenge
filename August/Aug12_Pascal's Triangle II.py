"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
def getRow(self, rowIndex):
    tri = [[1]]
    for i in range(1, rowIndex + 1):
        tri[0].append(0)
        for j in range(i, 0, -1):
            if j == i:
                tri[0][j] = 1
            else:
                tri[0][j] += tri[0][j - 1]
    return tri[0]