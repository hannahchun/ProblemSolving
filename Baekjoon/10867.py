# https://www.acmicpc.net/problem/10867
# Solution 1
# Python

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

res_list = []

for i in range(n-1) : 
    if nums[i] != nums[i+1] :
        print(nums[i], end=" ")
print(nums[n-1])