# https://leetcode.com/problems/plus-one/ 
# Solution 2
# Python

class Solution:
    def plusOne(self,digits) : 
        digits[len(digits)-1] +=1 # Increase the last element in 'digits' by 1
        for i in range(len(digits)-1,-1,-1) : # starting from the last element to the first element
            if digits[i] == 10 : # If an element is 10,
                digits[i]=0 # change it to 0
                if i==0 : # If the index is 0
                    digits.insert(0,1) # insert 1 at the beginning
                else :
                    digits[i-1]+=1 # increase the element before it
        return digits

sol1=Solution()
print(Solution.plusOne(sol1,[4,3,2,1]))

sol2=Solution()
print(Solution.plusOne(sol2,[9,9,9]))
