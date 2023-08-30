# https://leetcode.com/problems/two-sum/description/ 
# Solution 1
# Python

class Solution(object):
    def twoSum(self, nums, target):
        remain = {}
        for i in range(len(nums)) :
            diff = target - nums[i]
            if diff in remain :
                return [remain[diff], i]
            else :
                remain[nums[i]] = i

sol1 = Solution()
print(Solution.twoSum(sol1, [2, 7, 11, 15], 9))
print(Solution.twoSum(sol1, [3, 2, 4], 6))
print(Solution.twoSum(sol1, [1, 5, 6, 2, 0], 7))