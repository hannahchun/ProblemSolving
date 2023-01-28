# https://www.acmicpc.net/problem/1541
# Solution 1
# Python

eq = input().split('-')
res = 0

for i in eq[0].split('+') :
    res += int(i)

for i in eq[1:] :
    for j in i.split('+') :
        res -= int(j)
print(res)