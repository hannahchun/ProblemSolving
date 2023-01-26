# https://leetcode.com/problems/range-sum-query-immutable/
# Solution 1
# Python

from typing import List

class NumArray :

    def __init__(self, nums: List[int]) :
        self.nums = nums # nums라는 인스턴스 변수 생성하고 내용은 전달받은 parameter로 초기화

    def sumRange(self, left: int, right: int) -> int :
        return sum(self.nums[left : right + 1])

obj = NumArray([-2, 0, 3, -5, 2, -1])
idx = [[0, 2], [2, 5], [0, 5]]
res_list = ['null']

for i in range(0, len(idx)) :
    param_1 = obj.sumRange(idx[i][0], idx[i][1])
    res_list.append(param_1)
print(res_list)
