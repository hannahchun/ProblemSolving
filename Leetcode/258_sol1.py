# https://leetcode.com/problems/add-digits/
# Solution 1
# Python

class Solution:
    def addDigits(self, num: int) :
        while True :
            if num // 10 < 1 : # If the quotient when num is divided by 10 is smaller than 1, 
                return num # return!
            num_list=list(map(int,list(str(num))))
            # If not, convert num to string and turn it into a list 
            # ex. list(str(num))): ['3', '8']
            # To change it into a list with integer elements,
            # Use map() 
            # list(map(int,list(str(num)))): [3, 8]           
            sum_num=sum(num_list) # compute the sum of the elements in 'num_list'
            num=sum_num

sol1=Solution
print(Solution.addDigits(sol1,38))