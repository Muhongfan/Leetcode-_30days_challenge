
"""
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.


Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false


Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
"""
def __init__(self, characters, combinationLength):
    """
    :type characters: str
    :type combinationLength: int
    """
    # sorted the string
    characters = ''.join(sorted(characters))
    # combine character according to combinationlength
    self.charcombine = self.combine(characters, combinationLength)
    self.i = 0


def combine(self, characters, length):
    if length == 1:
        return [k for k in characters]
    res = []
    for i in range(len(characters) - length + 1):
        strs = self.combine(characters[i + 1:], length - 1)
        for stri in strs:
            res.append(characters[i] + stri)
    return res


def next(self):
    """
    :rtype: str
    """
    self.i += 1
    return self.charcombine[self.i - 1]


def hasNext(self):
    """
    :rtype: bool
    """
    if self.i < len(self.charcombine):
        return True
    else:
        return False


"""
首先将字母按字典排序
每个组合的字符串的长度为 combinationLength ， 
如果从原始字符串characters 选了第一个字母作为组合字符串的第一个字母，那么只能从剩下的字符串里面选择 
combinationLength-1个字符串的组合， 这就是一个递归。
这个递归的停止条件为，当只需要从剩下的字符串里面选一个字符（combinationLength == 1）的时候，直接返回所有可能的单个字符。
"""



#demo
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.characters = characters
        self.combinationLength = combinationLength
        self.counter = 0
        self.combs = list(combinations(sorted(characters), combinationLength))

    def next(self):
        """
        :rtype: str
        """
        res = ""
        comb = self.combs
        val = comb[self.counter]
        for i in val:
            res = res + i[1:]
        self.counter += 1
        return ''.join(val)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.counter > len(self.combs) - 1:
            return False
        else:
            return True
