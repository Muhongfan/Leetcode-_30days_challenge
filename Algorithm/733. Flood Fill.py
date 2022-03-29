class Solution(object):

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        R = len(image)
        C = len(image[0])
        if color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r - 1, c)
                if r + 1 < R: dfs(r + 1, c)
                if c >= 1: dfs(r, c - 1)
                if c + 1 < C: dfs(r, c + 1)

        dfs(sr, sc)
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] != newColor:
            targetPixel = [(sr, sc - 1), (sr, sc + 1), (sr - 1, sc), (sr + 1, sc)]
            old = image[sr][sc]
            image[sr][sc] = newColor
            for i, j in targetPixel:
                if i in range(len(image)) and j in range(len(image[i])) and image[i][j] == old:
                    self.floodFill(image, i, j, newColor)

        return image