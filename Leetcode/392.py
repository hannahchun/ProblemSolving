# https://leetcode.com/problems/is-subsequence/
# Solution 1
# Python

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)

        if len_s == 0 :
            return True
        
        cnt = 0
        for w in t :
            if w == s[cnt] :
                cnt += 1

                if cnt == len_s :
                    return True
        return False

sol1=Solution()
print(Solution.isSubsequence(sol1,"abc","ahbgdc"))

sol2=Solution()
print(Solution.isSubsequence(sol2,"ab","baab"))

sol3=Solution()
print(Solution.isSubsequence(sol2,"","huio"))