"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        #return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """

        return Counter(s) == Counter(t)
