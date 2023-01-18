# https://leetcode.com/problems/binary-search/
# Solution 1
# Python

class Solution :
    def search(self, nums, target) :
        for i in range(len(nums)) :
            if target == nums[i] :
                idx = i
                return idx
        return -1

sol1=Solution()
print(Solution.search(sol1,[-1,0,3,5,9,12], 9))

sol2=Solution()
print(Solution.search(sol2,[-1,0,3,5,9,12], 2))