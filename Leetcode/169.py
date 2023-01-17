# https://leetcode.com/problems/majority-element/
# Solution 1
# Python

class Solution:
    def majorityElement(self, nums) :
        keys = set(nums) # convert 'nums' to a set so as to keep distinct elements
        answer = 0

        for key in keys : # for each element in the set, 
            if nums.count(key) > len(nums) / 2 : # if the total number of that element in 'nums' is greater than the length of 'nums' divided by 2,
                answer = key # that element is the answer
                break
        return answer

sol1=Solution()
print(Solution.majorityElement(sol1,[3,2,3]))
print(Solution.majorityElement(sol1,[2,2,1,1,1,2,2]))
print(Solution.majorityElement(sol1,[6,5,5]))
print(Solution.majorityElement(sol1,[8,8,7,7,7]))