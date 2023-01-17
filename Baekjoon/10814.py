# https://www.acmicpc.net/problem/10814
# Solution 1
# Python

l = [input().split() for i in range(int(input()))]
l.sort(key=lambda x : int(x[0])) # Sort the list based on the first item of each list

for i in range(len(l)) :
    print(f'{l[i][0]} {l[i][1]}')

"""
<Example>

input:
3
21 Junkyu
21 Dohyun
20 Sunyoung

'l'= [['21', 'Junkyu'], ['21', 'Dohyun'], ['20', 'Sunyoung']]

sorted result:
20 Sunyoung
21 Junkyu
21 Dohyun

"""

"""

list.sort() vs the built-in function sorted()

Similarities!
: Both list.sort() and sorted() have the same key and reverse optional arguments

Differences!

list.sort() 
: sorts the list in-place, mutating its indexes and returning None
: can only be used with lists

sorted()
: returns a new sorted list leaving the original list unchanged
: accepts any iterable (e.g. list, tuple, dictionary, string)

Ex. nums = [2, 3, 1, 5, 6, 4, 0]

print(sorted(nums))   # [0, 1, 2, 3, 4, 5, 6]
print(nums)           # [2, 3, 1, 5, 6, 4, 0]

print(nums.sort())    # None
print(nums)           # [0, 1, 2, 3, 4, 5, 6]

Reference
: https://www.30secondsofcode.org/articles/s/python-sortedlist-vs-list-sort

"""