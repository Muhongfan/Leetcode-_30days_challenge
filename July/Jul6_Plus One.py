"""

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    s = ''
    for i in digits:
        s = s + str(i)
    s = str(int(s) + 1)
    output = []
    for i in range(len(s)):
        output.append(int(s[i]))
    return output

def plusOne(digits):
    digits[len(digits)-1] = digits[len(digits)-1]+1
    if digits[len(digits)-1] == 10:
        digits[len(digits)-1] =1
        digits.append(0)
    return digits


print(plusOne([1,9]))

