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