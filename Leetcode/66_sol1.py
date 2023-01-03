# https://leetcode.com/problems/plus-one/ 
# Solution 1
# Python

class Solution :
    def plusOne(self, digits) :
        length=len(digits)
        num=0
        # Combine the digits into one integer number (ex. [1,2,3] -> 123)
        for i in range(1, length+1) :
            num+=digits[i-1]*(10**(length-i))
        num+=1 # increase 1

        res=[]
        strNum=str(num) # Convert into a string
        # Convert each letter into an integer and add into 'res'
        for i in range(len(strNum)) :
            res.append(int(strNum[i]))
        return res

sol1=Solution()
print(Solution.plusOne(sol1,[4,3,2,1]))

sol2=Solution()
print(Solution.plusOne(sol2,[9,9]))