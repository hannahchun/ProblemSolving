# https://leetcode.com/problems/assign-cookies/
# Solution 1
# Python

class Solution :
    def findContentChildren(self,g,s) :
        num = 0 # The number of content children
        for i in range(len(s)) : # For each cookie,
            p=0 # a variable to store the greed factor of a child content with the cookie
            for j in range(len(g)) : # For each child,
                if g[j]<=s[i] : # Check whether cookie size is equal or greater than greed factor 
                    if p<g[j] : # Give the cookie to the child with a larger greed factor
                        p=g[j] # Save the greed factor of the child who recieved the cookie
                        idx=j # Save the index of the child who recieved the cookie
            if p!=0 : # If a child received a cookie
                num+=1 # increase 'num'
                g.pop(idx) # remove the greed factor of that child from the list
        return num

sol1=Solution()
print(Solution.findContentChildren(sol1,[1,2,3],[2,1]))

sol2=Solution()
print(Solution.findContentChildren(sol2,[1,2,3],[3])) 

sol3=Solution()
print(Solution.findContentChildren(sol3,[1,2],[1,2,3]))

sol4=Solution()
print(Solution.findContentChildren(sol4,[1,2,3],[1,2,3]))