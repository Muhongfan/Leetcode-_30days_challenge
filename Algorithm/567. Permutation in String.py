"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

# with array
def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """

    k = len(s1)
    s1 = ''.join(sorted(list(s1)))

    for i in range(len(s2)):
        sub = s2[i:i+k]
        sub_str = ''.join(sorted(list(sub)))
        if s1 == sub_str:
            return True
    return False
# with string
def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """

    k = len(s1)
    sub = Counter(s1)

    for i in range(len(s2)):
        if Counter(s2[i: i+k]) == sub:
            return True
    return False

