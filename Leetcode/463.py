# https://leetcode.com/problems/island-perimeter/
# Solution 1
# Python

from typing import List

class Solution :
    def islandPerimeter(self, grid: List[List[int]]) -> int :
        ans = 0
        for i in range(len(grid)) : 
            for j in range(len(grid[i])) : 
                if grid[i][j] == 1 : # 현재 검사하는 칸이 땅이면
                    # 그 땅의 상, 하, 좌, 우 검사
                    # matrix 범위를 넘어가거나, 물이 있으면 외곽선이 있다는 뜻이어서, 1을 더해
                    if i-1 < 0 or grid[i-1][j] == 0 : # 상
                        ans += 1
                    if i+1 >= len(grid) or grid[i+1][j] == 0 : # 하
                        ans += 1
                    if j-1 < 0 or grid[i][j-1] == 0 : # 좌
                        ans += 1
                    if j+1 >= len(grid[i]) or grid[i][j+1] == 0 : # 우
                        ans += 1
        return ans

a = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(a.islandPerimeter(grid))