# https://www.acmicpc.net/problem/5622
# Solution 1
# Python

dial=["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

a=input()

time=0 # total time spent

for i in range(len(a)) : # For each letter of the input, 
    for j in dial :  # For each element in 'dial',
        if a[i] in j : # If the element in 'dial' contains the letter in the input
            time+=dial.index(j) + 3 # increase the index of that element by 3  -> add the result to 'time'
print(time)