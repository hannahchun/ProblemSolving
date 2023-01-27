# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Solution 1
# Python

from typing import List

class KthLargest :

    def __init__(self, k: int, nums: List[int]) :
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int :
        self.nums.append(val)
        self.nums.sort(reverse = True)
        return self.nums[self.k-1]

obj = KthLargest(3, [4, 5, 8, 2])
idx = [3, 5, 10, 9, 4]
res_list = ['null']

for i in idx :
    param_1 = obj.add(i)
    res_list.append(param_1)
print(res_list)
