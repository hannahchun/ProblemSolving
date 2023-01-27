# https://leetcode.com/problems/baseball-game/description/
# Python
# Solution 1

from typing import List

class Solution :
    def calPoints(self, operations: List[str]) -> int :
        res = []
        for i in operations :
            if i == '+' :
                res.append(res[-1] + res[-2])
            elif i == 'D' :
                res.append(res[-1] * 2)
            elif i == 'C' :
                res.pop() # If the argument is omitted, the last item is deleted.
            else :
                res.append(int(i))
        return sum(res)

sol1 = Solution()
print(sol1.calPoints(["5", "2", "C", "D", "+"]))