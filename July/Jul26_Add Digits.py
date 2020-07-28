"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9
#print(addDigits(38))
# 归纳
def addDigits2(num):
    if num == 0:
        return 0
    else:
        return 1 + (num - 1) % 9

#设一个数是abcde，则abcde = a * 10000 + b * 1000 + c * 100 + d * 10 + e,
# 将这个式子拆一下得到(a + b + c + d + e) + (a * 9999 + b * 999 + c * 99 + d * 9)
def add(num):
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9

print(add(38))

