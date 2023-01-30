# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Solution 2
# Python

from typing import List

class Solution :
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
    
        for n in nums1 :
            if n in nums2 :
                res.append(n)
                nums2.remove(n)
        return res

sol1 = Solution()
print(Solution.intersect(sol1, [1, 2, 2, 1], [2, 2]))