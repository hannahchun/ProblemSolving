# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Solution 1
# Python

class Solution:
    def removeDuplicates(self,nums) :
        if len(nums) == 0 :
            return 0
        i = 0
        for j in range(1, len(nums)) :
            if nums[i] != nums[j] : # if the two numbers are different, 
                i += 1 # to put nums[j] in nums[i]
                nums[i] = nums[j]
        return i+1

sol1=Solution()
print(Solution.removeDuplicates(sol1,[1,2,3,3,4,5,6,6,7]))

sol2=Solution()
print(Solution.removeDuplicates(sol2,[0,0,1,1,1,2,2,3,3,4]))

"""
<Example>

input: [1,2,3,3,4,5,6,6,7] 
result list: [1,2,3,4,5,6,7,6,7]

"""