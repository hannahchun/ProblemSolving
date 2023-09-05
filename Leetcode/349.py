# https://leetcode.com/problems/intersection-of-two-arrays/
# Solution 1
# Python

class Solution(object):
    def intersection(self, nums1, nums2):
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        
        return list(set(nums1).intersection(nums2))
    
sol1=Solution()
print(Solution.intersection(sol1, [1,2,2,1], [2,2]))
print(Solution.intersection(sol1, [4,9,5], [9,4,9,8,4]))