# https://leetcode.com/problems/flood-fill/
# Solution 1
# Python

from typing import List

class Solution :
    def floodFill (self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]] :
        def dfs(i, j) :
            image[i][j] = newColor 
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] :
                if 0 <= x < m and 0 <= y < n and image[x][y] == f_color :
                    dfs(x, y)
        f_color, m, n = image[sr][sc], len(image), len(image[0])
        if f_color != newColor :
            dfs(sr, sc)
        return image

sol1=Solution()
print(Solution.floodFill(sol1, [[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))