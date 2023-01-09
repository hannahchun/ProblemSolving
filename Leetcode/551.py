# https://leetcode.com/problems/student-attendance-record-i/
# Solution 1
# Python

class Solution:
    def checkRecord(self, List) -> bool:
        absent=0 # The number of absences
        for i in range(len(List)) : # For each element in 'List',
            if i < len(List)-2 : # the starting index of 3 consecutive elements
                if List[i]=='L' and List[i+1]=='L' and List[i+2]=='L' : # If the elements are all 'L', the student was late for 3 consecutive days
                    return False
            if List[i]=='A' : 
                absent+=1
                if absent==2 : # If the student was absent for 2 days or more,
                    return False
        return True

sol1=Solution()
print(Solution.checkRecord(sol1, "PPALLP"))

sol2=Solution()
print(Solution.checkRecord(sol2, "PPALLL"))