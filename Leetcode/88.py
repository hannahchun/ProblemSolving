# https://leetcode.com/problems/merge-sorted-array/
# Solution 1
# Python

class Solution :
    def merge(self, nums1, m, nums2, n) :
        del nums1[m: ] # nums1의 m번째 원소부터 끝까지 삭제
        for i in range(n) : # nums2 원소를 nums1에 추가
            nums1.append(nums2[i])
        nums1.sort() # nums1 오름차순 정렬
        return nums1

sol1=Solution
print(Solution.merge(sol1,[1,2,3,0,0,0],3,[2,5,6],3))

sol2=Solution
print(Solution.merge(sol2,[1,2,3,4,0,0,0,0],4,[1,4,5,7],4))

sol3=Solution
print(Solution.merge(sol3,[0],0,[1],1))