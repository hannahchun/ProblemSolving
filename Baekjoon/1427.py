# https://www.acmicpc.net/problem/1427
# Solution 1
# Python

n = input()
n_list = []

n_list = list(map(int, str(n)))
# convert 'n' into string type 
# apply the int() function to each character in the string using the map() function and convert it into a list

n_list.sort(reverse=True)
# sort the elements in the list in descending order

for a in n_list :
    print(a, end="")