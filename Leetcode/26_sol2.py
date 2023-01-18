# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Solution 2
# Python

class Solution:
    def removeDuplicates(self,nums) :
        temp = list(set(nums)) # convert the type of 'nums' (list->set->list) to store non duplicate elements in a new list, 'temp'
        temp.sort() # sort them in ascending order

        for i, v in enumerate(temp) : # add the elements in 'temp' to the original list, 'num' 
            nums[i] = v # i: index of each element, v: each element
        return len(temp)

sol1=Solution()
print(Solution.removeDuplicates(sol1,[1,2,3,3,4,5,6,6,7]))

sol2=Solution()
print(Solution.removeDuplicates(sol2,[0,0,1,1,1,2,2,3,3,4]))