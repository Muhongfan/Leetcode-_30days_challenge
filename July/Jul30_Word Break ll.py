"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

# dp + dfs
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        Solution.res = []
        self.dfs(s, wordDict, '')
        return Solution.res

    def dfs(self, s, wordDict, stringlist):
        if self.check(s, wordDict):
            if len(s) == 0:
                Solution.res.append(stringlist[1:])
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    print(stringlist+' '+s[:i])
                    self.dfs(s[i:], wordDict, stringlist+' '+s[:i])

    def check(self, s, wordDict):
            dp = [False for i in range(len(s)+1)]
            dp[0] = True
            for i in range(len(s)):
                for j in range(i, -1, -1):
                    if dp[j] and s[j:i + 1] in wordDict:
                        dp[i + 1] = True
                        break
            return dp[len(s)]

solu = Solution()
print(solu.wordBreak("catsanddog",["cat","cats","and","sand","dog"]))


def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    n = len(s)
    if not n:
        return []
    dp = [[] for _ in range(n)]
    letters1 = set(c for c in s)
    letters2 = set(c for word in wordDict for c in word)
    if not letters2.issuperset(letters1):
        return []
    dic = set(wordDict)
    for i in range(0, n):
        for j in range(0, i + 1):
            cur_word = s[j:i + 1]
            if cur_word in dic:
                if j == 0:
                    dp[i].append(cur_word)
                else:
                    for sentence in dp[j - 1]:
                        dp[i].append(sentence + ' ' + cur_word)
    return dp[n - 1]