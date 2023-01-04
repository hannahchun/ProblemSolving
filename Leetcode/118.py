# https://leetcode.com/problems/pascals-triangle/
# Solution 1
# Python

n = int(input())
a = []

for i in range(n) :
    a.append([])
    a[i].append(1) # Add element 1 in the beginning of each row

    for j in range(1,i) : # Calculate the sum of the two numbers directly above (in the Pascal's triangle)
        a[i].append(a[i-1][j-1] + a[i-1][j])
    
    if (i!=0) : # Except the first row, 
        a[i].append(1) # add element 1 in the end of each row
print(a)