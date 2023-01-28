# https://www.acmicpc.net/problem/16435
# Solution 1
# Python

N, L = map(int, input().split())
fruit = list(map(int, input().split()))

fruit.sort() 

for i in range(N) :
    if fruit[i] <= L :
        L += 1
print(L)