# https://leetcode.com/problems/happy-number/
# Solution 1
# Python

class Solution(object):
    def isHappy(self, n):
        data = []
        while n != 1 :
            sum = 0
            string = str(n)
            for i in string :
                sum += int(i)**2
            if sum in data :
                return False
            else :
                data.append(sum)
                n = sum
        return True

sol1=Solution
print(Solution.isHappy(sol1, 19))
print(Solution.isHappy(sol1, 2))
