"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""
def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    l = len(s)
    for length in range(1, l // 2 + 1):
        if l % length == 0:
            sub = s[:length]
            repeat = l // length
            if sub * repeat == s:
                return True

    return False

print(repeatedSubstringPattern('abab'))


def repeatedSubstringPattern(self, s):
    """
    :type s: str
    :rtype: bool
    """
    return s in (s + s)[1:-1]