# https://www.acmicpc.net/problem/17212
# Solution 1
# Python

import sys
input = sys.stdin.readline

n = int(input())

dp = [e for e in range(n + 1)]

for i in range(2, n + 1) :
    dp[i] = dp[i - 1] + 1
    if i >= 2 :
        dp[i] = min(dp[i], dp[i - 2] + 1)
    if i >= 5 :
        dp[i] = min(dp[i], dp[i - 5] + 1)
    if i >= 7 :
        dp[i] = min(dp[i], dp[i - 7] + 1)
print(dp[n])