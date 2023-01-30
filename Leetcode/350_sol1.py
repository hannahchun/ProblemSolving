# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Solution 1
# Python

from typing import List
from collections import Counter

class Solution :
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        cnt = dict(Counter(nums1))
        # Counter()를 이용하여 nums1에 있는 각 요소가 몇 번씩 등장하는지 계산
        # dict()를 이용하여 사전 형식으로 나타냄 
        # Ex. {1: 2, 2: 2}

        for n in nums2 :
            if n in cnt and cnt[n] != 0 :
                res.append(n)
                cnt[n] -= 1
        return res

sol1 = Solution()
print(Solution.intersect(sol1, [1, 2, 2, 1], [2, 2]))