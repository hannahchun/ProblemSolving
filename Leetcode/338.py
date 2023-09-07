# https://leetcode.com/problems/counting-bits/
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

sol1=Solution()
print(Solution.countBits(sol1, 2))
print(Solution.countBits(sol1, 5))