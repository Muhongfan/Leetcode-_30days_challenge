"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

def backspaceCompare(S,T):
    S = list(S)
    T = list(T)
    out_S = []
    out_T = []
    for i, _ in enumerate(S):
        if _ == '#':
            out_S.remove(out_S[i - 1])

        else:
            out_S.append(_)
    for j, _ in enumerate(T):
        if _ == '#':
            out_T.remove(out_T[j - 1])

        else:
            out_T.append(_)
    if str(out_S) & str(out_T) == 1:
        return True
    else:
        return False

print(backspaceCompare("ab#c","ad#c"))
