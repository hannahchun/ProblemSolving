# https://leetcode.com/problems/climbing-stairs/
# Solution 1
# Python

class Solution(object):
    def climbStairs(self, n):
        dp = [0, 1, 2]
        
        if  n < len(dp) :
            return dp[n]
        
        for i in range(3, n + 1) :
            way = dp[i - 1] + dp[i - 2]
            dp.append(way)
        
        return dp[n]

sol1=Solution()
print(Solution.climbStairs(sol1, 2))
print(Solution.climbStairs(sol1, 3))
print(Solution.climbStairs(sol1, 4))