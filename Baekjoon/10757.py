# https://www.acmicpc.net/problem/10757
# Solution 1
# Python

num=input()
for i in range(len(num)) :
    if (num[i] == ' ') : # Find the space
        idx=i # Save the index of the space
        break
a=int(num[:idx])
b=int(num[idx+1:])
print(a+b)
