# https://leetcode.com/problems/sort-array-by-parity-ii/description/
# Solution 1
# Python

from typing import List

class Solution :
    def sortArrayByParityII(self, nums: List[int]) -> List[int] :
        j = 1
        for i in range(0, len(nums), 2) :
            if nums[i] % 2 : # 홀수인 경우만 실행
                while nums[j] % 2 : # 홀수인 경우만 실행
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums

sol1 = Solution()
print(sol1.sortArrayByParityII([4, 2, 5, 7]))