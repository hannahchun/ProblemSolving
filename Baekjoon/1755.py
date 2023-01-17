# https://www.acmicpc.net/problem/1755 
# Solution 1
# Python

d={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','0':'zero'}
m,n = map(int, input().split())

res=[] # 2 dimensional list to store the result [  [number, number name in English], ..   ] 

for i in range(m, n+1) : # For numbers from m to n, 
    s = ''
    for j in str(i) : # convert each number into a string
        s += d[j] # Find the corresponding name in English for each digit of the number
    res.append([i,s]) # add to 'res'
res.sort(key=lambda x:x[1]) # Sort the list based on the 2nd item of each list

# Print the numbers in the list
for i in range(len(res)) : 
    if i%10 == 0 and i!=0 :
        print()
    print(res[i][0], end=" ")
