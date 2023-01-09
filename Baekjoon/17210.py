# https://www.acmicpc.net/problem/17210
# Solution 1
# Python

"""
<Rules>
Impossible to use the same method two times in a row
Multiple of 2 must use the same method: 2,4,6,8,....
Multiple of 3 must use the same method: 3,6,9,....

-> Impossible to open the 6th door!
"""

num=int(input())
a=int(input())

if num>=6 : # If input is greater than 6,
    print("Love is open door") # cannot open the door
else :
    for i in range(num-1) :
        a = int(not a) # Use a method different from the previous step
        print(a)
