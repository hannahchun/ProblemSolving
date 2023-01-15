# https://www.acmicpc.net/problem/2164
# Solution 1
# Python

from collections import deque

deq = deque(list(range(1, int(input())+1)))

while len(deq) > 1 : # until the length of queue is longer than 1
    deq.popleft() # removes an element from the left side of the deque (If the deque is empty, popleft() will raise IndexError)
    deq.append(deq.popleft()) # pop and append to the right side of the deque
print(deq.popleft())



"""
<Deque in Python>
: implemented using the module “collections“
: a double-ended queue in which elements may be appended to or removed from either end
: is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.

Operations
1. append(): used to insert the value in its argument to the right end of the deque.
2. appendleft(): used to insert the value in its argument to the left end of the deque.
3. pop(): used to delete an argument from the right end of the deque.
4. popleft(): used to delete an argument from the left end of the deque.

Reference
: https://www.geeksforgeeks.org/deque-in-python/ 

"""
