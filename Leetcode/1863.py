# https://leetcode.com/problems/sum-of-all-subset-xor-totals
# Solution 1
# Python

class Solution:
    def subsetXORSum(self, nums) :
        def sums(term, idx) :
            if idx == len(nums) :
                return term
            return sums(term, idx + 1) + sums(term ^ nums[idx], idx + 1)
        return sums(0, 0)

sol1=Solution()
print(sol1.subsetXORSum([1,3]))
print(sol1.subsetXORSum([5,1,6]))
print(sol1.subsetXORSum([3,4,5,6,7,8]))