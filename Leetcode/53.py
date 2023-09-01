# https://leetcode.com/problems/maximum-subarray/
# Solution 1
# Python

class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)) :
            nums[i] = nums[i] + (nums[i - 1] if nums[i - 1] > 0 else 0)
        return max(nums)

sol1=Solution()
print(Solution.maxSubArray(sol1, [-2,1,-3,4,-1,2,1,-5,4]))
print(Solution.maxSubArray(sol1, [5,4,-1,7,8]))
print(Solution.maxSubArray(sol1, [1,-5,4,8,-9,10]))
print(Solution.maxSubArray(sol1, [7,5,-4,-3,9,1]))
