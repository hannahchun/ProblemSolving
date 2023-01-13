# https://leetcode.com/problems/valid-palindrome/
# Solution 1
# Python

class Solution:
    def isPalindrome(self, s) :
        strs="" # final string to check whether it's a valid palindrome 
        for i in range(len(s)) : # for each letter in the input, 
            if s[i].isalpha() : # if it's an alphabet, 
                strs += s[i].lower() # convert it into a lowercase and include it in 'strs'
            elif s[i].isdigit() : # if it's a number, 
                strs += s[i]
        rs = strs[::-1] # reverse 'strs'
        if strs == rs : # if 'strs' and reversed 'strs' are the same, 
            return True # valid palinrome 
        else :
            return False

sol1=Solution()
print(Solution.isPalindrome(sol1,"A man, a plan, a canal: Panama"))






sol1=Solution()
print(Solution.isPalindrome(sol1,"A man, a plan, a canal: Panama"))