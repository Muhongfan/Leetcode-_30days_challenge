"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

"""
import itertools


class Solution(object):
    # def countNegatives(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     count = 0
    #     for item in grid:
    #         for it in item:
    #             if it < 0:
    #                 count +=1
    #     return count
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num = 0
        for item in grid:
            for i in range(len(item)):
                if item[i] < 0:
                    num += len(grid[0]) - i
                    break
        return num
    #
    # def countNegatives(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     flat = itertools.chain.from_iterable(grid)
    #     count = 0
    #     for elem in flat:
    #         if elem < 0:
    #             count += 1
    #     return count

    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        num = 0
        for item in grid:
            for i in range(len(item)):
                if item[i] < 0:
                    num += len(grid[0]) - i
                    break


        return num

so = Solution()
print(so.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))