# https://www.acmicpc.net/problem/2920
# Solution 2
# Python

import copy 

scale = input().split()
scale2 = copy.deepcopy(sorted(scale)) # For comparison, sort the numbers in ascending order and implement deepcopy()

# Compare 'scale' and 'scale2'
if scale == scale2 :
    print("ascending")
elif scale == list(reversed(scale2)) :
    print("descending")
else :
    print("mixed")

# Module copy
# 1. copy.copy(x) : x의 얕은 복사결과를 반환, additional operation on the original one also affects the copied one.
# 2. copy.deepcopy(x) : x의 깊은 복사결과를 반환, additional operation on the original does not affect the copied one.