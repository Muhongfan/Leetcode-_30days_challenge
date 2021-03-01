"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.





Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

"""


def checkStraightLine(coordinates):
    """
    :type coordinates: List[List[int]]
    :rtype: bool
    """
    d = {}
    n = len(coordinates)

    x1 = coordinates[1][0] - coordinates[0][0]
    y1 = coordinates[1][1] - coordinates[0][1]
    for i in range(2, n, 1):
        x2 = coordinates[i][0] - coordinates[i - 1][0]
        y2 = coordinates[i][1] - coordinates[i - 1][1]
        if (x1 * y2 != x2 * y1):
            return False
    return True


class Solution(object):
    def checkStraightLine(self, coordinates):

        first = coordinates[0]
        second = coordinates[1]

        i = 2
        while i < len(coordinates):
            if self.slope_equality_check(first, second, coordinates[i]):
                return False
            i += 1

        return True

    def slope_calculate(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        if x1 == x2:
            return float("inf")
        slope = (float)(y2 - y1) / (x2 - x1)
        return slope

    def slope_equality_check(self, point1, point2, point3):
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3

        # ((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1))
        return ((y2 - y1) * (x1 - x3) != (y1 - y3) * (x2 - x1))
