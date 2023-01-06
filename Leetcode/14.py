# https://leetcode.com/problems/longest-common-prefix/
# Solution 1
# Python

class Solution :
    def longestCommonPrefix(self, List) :
        # Sort 'List' in ascending order according to the length of each element
        List.sort(key=lambda x : len(x))
        # List[0]: the element with the shortest length

        # If the 'List' is empty, return "" 
        if len(List) == 0 :
            return ""
        
        # If not,
        else :
            for i in range(len(List[0])) : # For each letter in 'List[0]'
                for j in range(1, len(List)) : # For each element in 'List' other than 'List[0]',
                    if List[0][i] != List[j][i] : # If the characters do not match in the same index,
                        return List[0][:i] # Stop comparison and return 
            return List[0] # If the longest common prefix == 'List[0]'
        
sol1=Solution()
print(Solution.longestCommonPrefix(sol1, ["flower","flow","flight"]))