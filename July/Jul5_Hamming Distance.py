"""

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.


"""
'''
Binary number and how to compute binary ones
'''
import math

def hammingDistance(x, y):
    res = max(x, y) ^ min(x, y)
    count = 0
    while res > 0 :
        count += res & 1
        res >>= 1
    return count
print(hammingDistance(1,4))


