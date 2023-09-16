# https://leetcode.com/problems/missing-number/
# Solution 1
# Python

class Solution :
    def missingNumber(self, nums) :
        set_result = set(range(0, len(nums) + 1))
        set_nums = set(nums)
        return list(set_result - set_nums)[0]

sol1=Solution()
print(Solution.missingNumber(sol1, [3,0,1])) 
print(Solution.missingNumber(sol1, [9,6,4,2,3,5,7,0,1])) 