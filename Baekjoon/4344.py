# https://www.acmicpc.net/problem/4344
# Solution 1
# Python

num=int(input())
ans=list() # a list to store the % of students above the average

for i in range(1, num+1) :
    a=list(map(int,input().split()))
    avg=sum(a[1:])/a[0] # Calculate the average of each line
    cnt=0 # a variable to store the number of students above the average
    for j in range(1,len(a)) :
        if a[j] > avg : # If the student is above the average
            cnt+=1 # increase 'cnt'
    ans.append(round(cnt/a[0]*100,3)) # Calculate the % of students above the average and add the result to 'ans'

for i in range(0,num) :
    print("{:.3f%".format(ans[i]))

# a=list(map(int,input().split())) 
# 1. input().split() : 띄어쓰기로 구분하여 문자열을 리스트로 만듦
# 2. list(map(int,input().split())) : 리스트의 값을 정수 타입으로 변환 (1st parameter : int(x) 함수, 2nd parameter : 리스트)
