# https://www.acmicpc.net/problem/1316 
# Solution 1
# Python

num=int(input())
total=0

for i in range(num) :
    s=input() 
    strList=[] # 중복되는 글자 체크 위한 리스트 
    total+=1 # 입력된 단어가 그룹단어라고 가정
    pre_j='' # 연속되는 글자 여부 확인 위해 이전 글자 저장
    for j in s :
        if j in strList and pre_j != j : # 이전에 나왔던 글자이지만, 바로 이전 글자와 같지 않은 경우, 
            total-=1 # 그룹단어가 아님
            break
        else :
            strList.append(j)
            pre_j=j
print(total)