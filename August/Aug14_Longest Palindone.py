"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: int
    """
    dict1 = {}
    j = 0
    z = 0
    for i in range(len(s)):
        if s[i] in dict1:
            dict1[s[i]] += 1
        else:
            dict1[s[i]] = 1
    for v in dict1:
        if (dict1[v] + 1) % 2 == 0:
            j += (dict1[v] - 1)
            z += 1
        if dict1[v] % 2 == 0: j += dict1[v]
    if z > 0:
        return j + 1
    else:
        return j