# https://www.acmicpc.net/problem/2920
# Solution 1
# Python

num = input()
num_list = num.split(' ')

isAscending = True 
isDescending = True 

for i in range(1, len(num_list)) :
    if num_list[i] < num_list[i-1] : 
        isAscending = False
    if num_list[i-1] < num_list[i] :
        isDescending = False
        
if isAscending == True :
    print("ascending")
elif isDescending == True :
    print("descending")
else :
    print("mixed")