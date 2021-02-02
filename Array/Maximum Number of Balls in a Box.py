"""
You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.



Example 1:

Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.
Example 2:

Input: lowLimit = 5, highLimit = 15
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
Boxes 5 and 6 have the most number of balls with 2 balls in each.
Example 3:

Input: lowLimit = 19, highLimit = 28
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
Box 10 has the most number of balls with 2 balls.


Constraints:

1 <= lowLimit <= highLimit <= 105
"""
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        #num = 0
        dic = dict()
        for i in range(lowLimit, highLimit+1):
            if i < 10:
                dic.setdefault(i, 1)
            else:
                num = self.isnotNull(i)
                if num in dic:
                    value = dic.get(num)
                    dic[num] = value + 1
                dic.setdefault(num, 1)
        #return max(dic.values())
        return max(dic.values())

    def isnotNull(self, i):
        num = 0
        while i:
            num += i % 10
            i //= 10
        return num
so = Solution()
#print(so.countBalls(220,548))
print(so.isnotNull(220))
print(220%10)


def countBalls(self, lowLimit, highLimit):
    """
    :type lowLimit: int
    :type highLimit: int
    :rtype: int
    """
    import collections
    ans, s = 0, 0
    d = collections.defaultdict(int)
    for i in range(lowLimit, highLimit + 1):
        if i % 10 > 0 and s:
            s += 1
        else:
            s = 0
            while i > 0:
                s += i % 10
                i //= 10
        d[s] += 1
        ans = max(ans, d[s])
    return ans

def countBalls(self, lo, hi):
    a = [0] * 50
    for x in xrange(lo, hi + 1):
        y = x
        s = 0
        while y:
            s += y % 10
            y /= 10
        a[s] += 1
    return max(a)

