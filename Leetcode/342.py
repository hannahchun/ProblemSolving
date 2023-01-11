# https://leetcode.com/problems/power-of-four/ 
# Solution 1
# Python

class Solution:
    def isPowerOfFour(self, n) :
        num=1
        while(num<n) : # multiply 'num' by 4 until 'n' is smaller than or same as 'num'
            num*=4
        if num == n : # if 'num' and 'n' are the same, 
            return True # 'n' is a power of four
        else :
            return False

sol1=Solution()
print(Solution.isPowerOfFour(sol1,16))

sol2=Solution()
print(Solution.isPowerOfFour(sol2,56))