# https://leetcode.com/problems/min-cost-climbing-stairs/
# Solution 1
# Python

class Solution(object):
    def minCostClimbingStairs(self, cost) :
        for i in range(2, len(cost)) :
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])
    
sol1=Solution()
print(Solution.minCostClimbingStairs(sol1, [10,15,20]))
print(Solution.minCostClimbingStairs(sol1, [1,100,1,1,1,100,1,1,100,1]))
        