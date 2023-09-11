# https://leetcode.com/problems/fibonacci-number/
# Solution 1
# Python

class Solution(object):
    def fib(self, n):
        if n == 0 :
            return 0
        if n == 1 :
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

sol1 = Solution()
print(sol1.fib(2))
print(sol1.fib(3))
print(sol1.fib(4))