# https://www.acmicpc.net/problem/11052
# Solution 1
# Python

N = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N + 1)] 
# N = 4이면, [0, 0, 0, 0, 0]

for i in range(1, N + 1) :
    for k in range(1, i + 1) :
        dp[i] = max(dp[i], dp[i - k] + p[k])
print(dp[i])
