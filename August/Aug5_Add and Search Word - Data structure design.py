"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class TrieNode(object):
    def __init__(self):
        self.childs = {}
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child == None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root,word)

    def find(self,node,word):
        if word == '':
            return node.isWord
        if word[0] == '.':
            for _,child in node.childs.items():
                if self.find(child,word[1:]):
                    return True
        elif word[0] in node.childs:
            return self.find(node.childs.get(word[0]),word[1:])
        return False
n = WordDictionary()
n.addWord("bad")
n.addWord("dad")
n.addWord("mad")
n.search("pad")