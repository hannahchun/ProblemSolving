# https://www.acmicpc.net/problem/11047
# Solution 1
# Python

n, k = map(int, input().split())
val = []
num = 0

for i in range(n) :
    a = input()
    val.append(a)

for i in range(n-1, -1, -1) :
    if int(val[i]) <= k : 
        n = k // int(val[i]) 
        k -= n * int(val[i]) 
        num += n
        if k == 0 :
            break
print(num)