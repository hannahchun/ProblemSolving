# https://programmers.co.kr/learn/courses/30/lessons/12977
# Solution 1 
# Python 

def solution(nums) :
    answer =0 # The number of prime numbers
    for i in range(len(nums)-2) :
        for j in range(i+1, len(nums)-1) :
            for z in range(j+1, len(nums)) :
                if (check(nums[i],nums[j],nums[z])) : # Call check() function (a user defined function)
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
