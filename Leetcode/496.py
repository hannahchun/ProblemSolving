# https://leetcode.com/problems/next-greater-element-i/
# Solution 1
# Python

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num1 in nums1 :
            found = False
            for num2 in nums2[nums2.index(num1):] :
                if num2 > num1 :
                    found = True
                    res.append(num2)
                    break
            if not found :
                res.append(-1)
        return res

sol1 = Solution()
print(sol1.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    