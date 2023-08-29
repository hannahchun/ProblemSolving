# https://school.programmers.co.kr/learn/courses/30/lessons/12914?language=python3
# Solution 1
# Python

def solution(n) :
    if n == 1 :
        return 1
    else :
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1) :
            dp[i] = dp[i - 2] + dp[i - 1]
    return dp[-1] % 1234567

print(solution(5))
print(solution(6))