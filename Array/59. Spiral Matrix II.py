"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]

"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[0] * n for _ in range(n)]

        def filling(counter, row_top, row_bottom, col_left, col_right):
            if row_top > row_bottom or col_left > col_right:
                return
            for col in range(col_left, col_right + 1):
                answer[row_top][col] = counter
                counter += 1
            for row in range(row_top + 1, row_bottom + 1):
                answer[row][col_right] = counter
                counter += 1
            for col in reversed(range(col_left, col_right)):
                answer[row_bottom][col] = counter
                counter += 1
            for row in reversed(range(row_top + 1, row_bottom)):
                answer[row][col_left] = counter
                counter += 1
            filling(counter, row_top + 1, row_bottom - 1, col_left + 1, col_right - 1)

        filling(1, 0, n - 1, 0, n - 1)
        return answer

