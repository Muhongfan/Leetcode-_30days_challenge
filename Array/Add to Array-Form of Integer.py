"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.



Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000


Note：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0

"""

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # list -> int
        #A = int("".join(map(str,A)))
        #answer = int("".join(map(str,A))) + K
        #int - > list : list(str(x)
        return list(str(int("".join(map(str,A))) + K))

    def addToArrayForm2(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # Time: O(logK * logA) Space: O(1)  Digits are O(logK) not O(K)!!
        if K == 0:
            return A

        carry, i = 0, len(A) - 1
        while K != 0 or carry != 0:  # Both the addition number have to be exhausted AND THERE MUST BE NO CARRY LEFT.
            if i == -1:
                A.insert(0, 0)
                i = 0
            digit = K % 10
            K //= 10
            check = A[i] + digit + carry
            if check >= 10:
                carry = 1
                A[i] = check % 10
            else:
                carry = 0
                A[i] = check
            i -= 1
        return A

so = Solution()
print(so.addToArrayForm([1,2,0,0],34))

