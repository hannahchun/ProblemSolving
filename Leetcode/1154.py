# https://leetcode.com/problems/day-of-the-year/
# Solution 1
# Python

"""

<Gregorian calendar>
Leap year 
: 4년에 한번씩 돌아오는 2월 29일이 있는 해
Every year that is exactly divisible by four, except for the years that are exactly divisible by 100, 
but these centurial years are leap years if they are exactly divisible by 400. 

"""

class Solution:
    def dayOfYear(self, date) :
        temp = date.split('-') # stores each element in a List
        year = int(temp[0])
        month = int(temp[1])
        day = int(temp[2])

        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # store days of each month

        ans = sum(days[:month-1]) + day

        # Check if its a Leap year
        if ((year%4 == 0 and year%100 != 0) or year%400 == 0) and month > 2 :
            ans +=1
        return ans

sol1=Solution()
print(Solution.dayOfYear(sol1,"2019-01-09"))

sol2=Solution()
print(Solution.dayOfYear(sol2,"2003-11-09"))      

sol3=Solution()
print(Solution.dayOfYear(sol3,"2004-03-01"))      

sol4=Solution()
print(Solution.dayOfYear(sol4,"2019-02-10"))
