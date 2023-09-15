# https://leetcode.com/problems/isomorphic-strings/
# Solution 1
# Python

class Solution:
    def isIsomorphic(self, s: str, t: str) :
        a = dict()
        b = dict()
        for a1, b1 in zip(s, t) :
            if (a1 not in a) and (b1 not in b) :
                a[a1] = b1
                b[b1] = a1
            elif a.get(a1) != b1 or b.get(b1) != a1 :
                return False
        return True

sol1=Solution()
print(Solution.isIsomorphic(sol1, "egg", "add"))
print(Solution.isIsomorphic(sol1, "foo", "bar"))
print(Solution.isIsomorphic(sol1, "paper", "title"))