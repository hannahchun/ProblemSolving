# https://leetcode.com/problems/valid-anagram/
# Solution 1
# Python

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
    
sol1=Solution()
print(Solution.isAnagram(sol1, "anagram", "nagaram"))
print(Solution.isAnagram(sol1, "rat", "car"))