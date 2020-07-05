"""

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.

"""

print(2%2)
def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int

    """

    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]:
            i2 += 1
        while ugly[i3] * 3 <= ugly[-1]:
            i3 += 1
        while ugly[i5] * 5 <= ugly[-1]:
            i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]

def thUglyNumber(n):

    L2 = 1
    L3 = 1
    L5 = 1
    li = []

    li.append(1)
    out = li.copy()
    while len(out) -1 < n:
        li.append(min(L2 * 2, min(L3 * 3, L5 * 5)))
        out = sorted(set(li), key=li.index)
        if out[-1] == L2 *2:
            L2 += 1
        if out[-1] == L3 *3:
            L3 += 1
        if out[-1] == L5 *5:
            L5 += 1
    print(li)
    print(out)
    return out[-1]

print(nthUglyNumber(10))