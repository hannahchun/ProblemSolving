# https://leetcode.com/problems/largest-perimeter-triangle/
# Solution 1
# Python

from typing import List

class Solution :
    def largestPerimeter(self, nums: List[int]) -> int :
        nums.sort(reverse = True) # 내림차순 정렬

        # 삼각형을 만들기 위해서는 가장 긴 변의 길이가 다른 두 변의 길이의 합보다 작은 경우가 있어야
        for i in range(len(nums) - 2) : 
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if a < b + c :
                return a + b + c
        return 0

sol1 = Solution()
print(Solution.largestPerimeter(sol1, [2, 1, 2]))

sol2 = Solution()
print(Solution.largestPerimeter(sol2, [3, 2, 3, 4]))

sol3 = Solution()
print(Solution.largestPerimeter(sol3, [1, 2, 1, 10]))
