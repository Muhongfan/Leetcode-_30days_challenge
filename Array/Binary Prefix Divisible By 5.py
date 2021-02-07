"""
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

Example 1:

Input: [0,1,1]
Output: [true,false,false]
Explanation:
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
Example 2:

Input: [1,1,1]
Output: [false,false,false]
Example 3:

Input: [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]
Example 4:

Input: [1,1,1,0,1]
Output: [false,false,false,false,false]


Note:

1 <= A.length <= 30000
A[i] is 0 or 1

"""
#暴力求解 - 超时

def prefixesDivBy51(A):
    """
    :type A: List[int]
    :rtype: List[bool]
    """
    A_list = []
    answer = []
    for i in A:
        A_list.append(i)
        num = int("".join(map(str,A_list)),2)

        if num % 5 == 0 :
            answer.append(True)
        else:
            answer.append(False)
    return answer



def prefixesDivBy5(A):
    """
    :type A: List[int]
    :rtype: List[bool]
    """
    A_list = []
    answer = []
    for i in A:
        A_list.append(i)
        answer.append(int("".join(map(str, A_list)), 2) % 5 ==0 )
    return answer
print(prefixesDivBy5([0,1,1,1,1,1]))


"""
求余的性质。我们每次只用保存前缀对5的余数，在求下一个位置的时候把上一次的前缀×2 + 当前的数字再模5.

求余的性质：

((a +b)mod p × c) mod p = ((a × c) mod p + (b × c) mod p) mod p
(a×b) mod c=((a mod c) * (b mod c)) mod c
(a+b) mod c=((a mod c)+ (b mod c)) mod c
(a-b) mod c=((a mod c)- (b mod c)) mod c
1
2
3
4
所以，a扩大x倍之后模一个数字，等于((a % 5) * (x % 5)) % 5.
"""
def prefixesDivBy5(A):
    """
    :type A: List[int]
    :rtype: List[bool]
    """
    res = []
    prefix = 0
    for a in A:
        prefix = (prefix * 2 + a) % 5
        res.append(prefix == 0)
    return res