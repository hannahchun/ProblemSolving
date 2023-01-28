# https://www.acmicpc.net/problem/15729
# Python
# Solution 1

n = int(input())
b = list(map(int, input().split()))
f = [0 for i in range(n)]
cnt = 0

for i in range(n) :
    if b[i] != f[i] :
        cnt += 1
        if b[i] == 0 :
            f[i] = 0 
        else :
            f[i] = 1
        if i <= n-3 :
            for j in range(i+1, i+3) :
                if f[j] == 0 :
                    f[j] = 1
                else :
                    f[j] = 0
        if i == n-2 :
            if f[n-1] == 0 :
                f[n-1] = 1
            else :
                f[n-1] = 0
print(cnt)
