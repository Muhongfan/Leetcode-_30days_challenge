"""
Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

"""


def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat
    res = []
    row = []
    for i in range(m):
        for j in range(n):
            row.append(mat[i][j])
            if len(row) == c:
                res.append(row)
                row = []
    return res