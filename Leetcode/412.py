# https://leetcode.com/problems/fizz-buzz/
# Solution 1
# Python

class Solution:
    def fizzBuzz(self, n) :
        ans = [] # a list to store the output
        for i in range(n) : 
            if ((i+1) %3 == 0) : # if the number is divisible by 3
                if ((i+1) %5 == 0) : # if the number is also divisible by 5
                    ans.append("FizzBuzz")
                else :
                    ans.append("Fizz")
            else : # if the number is not divisible by 3
                if ((i+1) %5 == 0) : # if the number is divisible by 5
                    ans.append("Buzz")
                else :
                    ans.append(str(i+1))
        return ans

sol1=Solution()
print(Solution.fizzBuzz(sol1, 15))