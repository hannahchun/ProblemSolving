# https://leetcode.com/problems/relative-sort-array
# Solution 1
# Python

from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2) :
        res = []
        for i in arr2 :
            res.extend([i] * Counter(arr1)[i])
        return res + sorted([i for i in arr1 if i not in res])

sol1 = Solution()
print(sol1.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
print(sol1.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))