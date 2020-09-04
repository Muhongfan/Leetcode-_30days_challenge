def repeatedSubstringPattern(self, s):
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