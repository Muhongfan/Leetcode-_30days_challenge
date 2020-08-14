
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
