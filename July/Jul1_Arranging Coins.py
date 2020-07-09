"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

"""
def arrangeCoins(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        for i in range(1, n):
            rest = n - i
            if rest > 0:
                n = rest
            else:
                break
            if rest < i + 1:
                return i
            elif rest == i + 1:
                return i + 1


print(arrangeCoins(3))

# demo solution
'''
Find the logic of the problem
'''
import math
def arrangecoins(N):
    return math.floor((-1 + math.sqrt(1 + 8 * N)) / 2)
