# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Solution 1
# Python

class Solution(object):
    def findDisappearedNumbers(self, nums):
        if len(nums) < 0 :
            answer = []
        else :
            max_num = len(nums)
            answer = list(set(range(1, max_num + 1)) - set(nums))
        return answer

sol1 = Solution()
print(Solution.findDisappearedNumbers(sol1, [4,3,2,7,8,2,3,1]))
print(Solution.findDisappearedNumbers(sol1, [1,1]))
print(Solution.findDisappearedNumbers(sol1, [5,3,5,2,2,5]))