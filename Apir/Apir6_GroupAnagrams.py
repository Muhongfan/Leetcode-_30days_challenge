"""
Group Anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
import collections


def groupAnagrams(strs):

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strs:
            tup = tuple(sorted(s))
            d[tup].append(s)
        return d.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


print(set("eat"))
# set(['a', 'e', 't'])

print(sorted("eat"))
# ['a', 'e', 't']