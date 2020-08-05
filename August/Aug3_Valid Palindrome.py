"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Constraints:

s consists only of printable ASCII characters.
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    i = -1
    j = len(s)
    while True:
        i += 1
        j -= 1
        if i > j:
            return True
        while i < j:
            if not s[i].isalnum():
                i += 1
            else:
                break
        while i < j:
            if not s[j].isalnum():
                j -= 1
            else:
                break
        if s[i].lower() != s[j].lower():
            return False
print(isPalindrome("A man, a plan, a canal: Panama"))