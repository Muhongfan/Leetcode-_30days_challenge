"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""


def validMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    m = max(arr)
    k = arr.index(m)
    if m == arr[0]:
        return False
    for i in arr[1:k:]:
        if i < i - 1:
            return False
        else:
            for j in arr[k::]:
                if j < j - 1:
                    return False
    return True

def validMountainArray(A):
    """
    :type A: List[int]
    :rtype: bool
        """
    N = len(A)
    if N < 3:
    return False
    i = 0
    while i < N - 1 and A[i + 1] > A[i]:
        i += 1
    if i == 0 or i == N - 1: return False
    while i < N - 1 and A[i] > A[i + 1]:
        i += 1
    return i == N - 1

def validMountainArray(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        p = arr[1]
        if arr[0] >= p:
            return False
        down = False
        for a in arr[2:]:
            if a == p:
                return False
            if down and a < p:
                p = a
                continue
            if down and a > p:
                return False
            if a < p:
                down = True

            p = a
        return down
print(validMountainArray([2,1]))