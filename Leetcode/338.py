# https://leetcode.com/problems/counting-bits/

"""
# O(nlogn)
# Solution 1 - Brute Force
# Python

class Solution(object):
    def countBits(self, n):
        results = [0] * (n + 1)
        
        for i in range(1, n + 1) :
            j = i
            while j != 0 :
                if j % 2 == 1 :
                    results[i] += 1
                j = j // 2 
        return results
"""
# O(n)
# Solution 2 - Dynamic Programming
# Python

class Solution(object):
    def countBits(self, n):
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1) :
            if offset * 2 == i :
                offset = i
            dp[i] = dp [i - offset] + 1
        return dp

sol1=Solution()
print(Solution.countBits(sol1, 2))
print(Solution.countBits(sol1, 5))
print(Solution.countBits(sol1, 6))