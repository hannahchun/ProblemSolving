# https://programmers.co.kr/learn/courses/30/lessons/12977
# Solution 2
# Python 

from itertools import combinations 

def solution(nums) :
    answer = 0 # The number of prime numbers
    L = list(combinations(nums,3)) # use combinations() in itertools and convert the result into a list
    for i in L :
        if(check(i[0],i[1],i[2])) : # Call check() function (a user defined function)
            answer+=1 
    return answer

def check(a,b,c) :
    res=a+b+c # Sums up the three numbers
    for k in range(2,res) : # Check whether it is divisible by the numbers from 2 to 'res'-1
        if (res % k == 0) : # if divisible,
            return False # not a prime number
    return True

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))


"""

<Itertools>
: a module provided by Python for creating iterators for efficient looping

combinations(iterable, r)
: returns r-length tuples of every possible selection (the second paramter is necessary)
Ex. chars = ['A', 'B', 'C'] 
    c = itertools.combinations(chars, 2) 
    print(list(c)) // [('A', 'B'), ('A', 'C'), ('B', 'C')]

permutations(iterable, r)
: returns r-length tuples of every possible ordering (the default of the second parameter is the length of the first parameter)
Ex. chars = ['A', 'B', 'C'] 
    p = itertools.permutations(chars, 2)
    print(list(p)) // [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

cf . combinations and permutations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the tuples will be produced in sorted order.

"""