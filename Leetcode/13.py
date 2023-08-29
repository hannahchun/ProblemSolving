# https://leetcode.com/problems/roman-to-integer/
# Solution 1
# Python

class Solution(object):
    def romanToInt(self, s):
        roman = {'M' : 1000, 'D' : 500, 'CM' : 900, 'CD' : 400, 'C' : 100, 'L' : 50, 'XC' : 90, 'XL' : 40, 'X' : 10, 'V' : 5, 'IX' : 9, 'IV' : 4, 'I' : 1}
        idx = 0
        value = 0
        while (idx < len(s)) :
            if (idx + 1) != len(s) and s[idx] + s[idx + 1] in roman :
                value += roman[s[idx] + s[idx + 1]]
                idx += 2
            else :
                value += roman[s[idx]]
                idx += 1
        return value

sol1=Solution()
print(Solution.romanToInt(sol1, "III"))
print(Solution.romanToInt(sol1, "LVIII"))
print(Solution.romanToInt(sol1, "MCMXCIV"))
print(Solution.romanToInt(sol1, "XCII"))