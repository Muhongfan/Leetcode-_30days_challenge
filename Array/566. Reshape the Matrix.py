"""
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.



Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

"""


def matrixReshape(mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    m = len(mat)
    n = len(mat[0])
    if m*n != r*c:
        return mat
    row = []
    col = []
    for i in range(m):
        for j in range(n):
            row.append(mat[i][j])
            if len(row) == c:
                col.append(row)
            row = []
    return col

def matrixReshape2(mat, r, c):
    m = len(mat)
    n = len(mat[0])
    if m * n != r * c:
        return mat
    reshaped = [[0] * c for _ in range(r)]
    for i in range(r*c):
        reshaped[i // c][i % c] = mat[i // n][i % n]

