"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""
def searchMatrix(matrix, target):
    m = len(matrix)
    if m == 0: return False
    n = len(matrix[0])

    left = 0
    right = m*n-1
    while left <= right:
        index = (left+right) // 2
        pivot = matrix[index //n][index%n]
        if pivot == target:
            return True
        else:
            if pivot < target:
                left +=1
            else:
                right-=1
    return False
class Solution(object):
    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        while n >=0:
            for i in matrix:
                if target in i:
                    return True
                n -=1
        return False

