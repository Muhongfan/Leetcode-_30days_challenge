"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
#回溯
def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    visited = [[False for j in range(len(board[0]))] for i in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if existRecu(board, word, 0, i, j, visited):
                return True
    return False


def existRecu(board, word, cur, i, j, visited):
    if cur == len(word):  # 如果到单词长度，结束。
        return True

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
        return False  # 越界或者是当前字母不等于word中对应位置字母

    # 如果到这说明对应位置有，继续从此位置遍历四个方向
    visited[i][j] = True
    result = existRecu(board, word, cur + 1, i + 1, j, visited) or \
             existRecu(board, word, cur + 1, i - 1, j, visited) or \
             existRecu(board, word, cur + 1, i, j + 1, visited) or \
             existRecu(board, word, cur + 1, i, j - 1, visited)
    visited[i][j] = False

    return result

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
