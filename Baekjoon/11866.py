# https://www.acmicpc.net/problem/11866
# Solution 1
# Python

n, k = map(int, input().split())
table = [i for i in range(1, n+1)] # 'n' people sitting around a table

answer = [] # save the number of the person removed from the table
idx = 0 # the index of the person removed

for x in range(n) :
    idx += k-1 # 'idx' needs to move to the 'k'th person 
    if idx >= len(table) : # if 'idx' is larger than the total number of remaining people
        idx = idx % len(table) # 'idx' = the remainder when 'idx' is divided by the total number of remaining people
    answer.append(str(table.pop(idx))) # remove the 'idx'th person from the table and add the number of the 'idx'th person to 'answer'

print("<", ", ".join(answer)[:], ">", sep='')
    