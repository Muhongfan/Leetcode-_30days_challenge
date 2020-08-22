"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""
def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    l, r = 0, len(A) - 1
    while l < r:
        if A[l] & 1:
            A[l], A[r] = A[r], A[l]
        l += not (A[l] & 1)
        r -= A[r] & 1
    return A

#demo
def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """

    even = []
    odd = []

    for num in A:
        if (num % 2 == 0):
            even.append(num)
        else:
            odd.append(num)

    return even + odd