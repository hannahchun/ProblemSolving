# https://leetcode.com/problems/valid-palindrome/
# Solution 2
# Python

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=[]
        for char in s :
            if char.isalnum() : # if the string consists of alphabet or numbers
                strs.append(char.lower()) # convert it into a lowercase and include it in 'strs'
        while len(strs) > 1 : # if the length of 'strs' is greater than 1,
            if strs.pop(0) != strs.pop() :
                return False
        return True

sol1=Solution
print(Solution.isPalindrome(sol1,"A man, a plan, a canal: Panama"))
