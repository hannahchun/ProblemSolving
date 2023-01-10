# https://www.acmicpc.net/problem/3052
# Solution 1
# Python

remainder_list = [] # a list to store the remainders

for i in range(10) :
    num=int(input())
    remainder=num%42 # Calculate the remainder when 'num' is divided by 42
    if remainder not in remainder_list : # if the remainder is not in 'remainder_list',
        remainder_list.append(remainder) # append the new remainder to 'remainder_list'

print(len(remainder_list))
