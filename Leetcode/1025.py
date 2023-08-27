# https://leetcode.com/problems/divisor-game/ 
# Solution 1
# Python

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

sol1 = Solution()
print(sol1.divisorGame(15))
print(sol1.divisorGame(16))