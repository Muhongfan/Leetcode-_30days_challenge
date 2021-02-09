"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].


Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4

"""


def hasGroupsSizeX(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    deck = sorted(deck)
    answer = [deck[:1]]
    [answer[-1].append(y) if x == y else answer.append([y]) for x, y in zip(deck[:-1], deck[1:])]
    if len(answer) <3:
        return False
    for i in range(1, len(answer)):

        if len(answer[i]) == len(answer[i - 1]):
            continue
            #return False
        else:
            return False
    return True

print(hasGroupsSizeX([1,1]))


def hasGroupsSizeX(self, deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    count = collections.Counter(deck)
    X = min(count.values())
    for x in range(2, X + 1):
        if all(v % x == 0 for v in count.values()):
            return True
    return False
