# https://www.acmicpc.net/problem/2953
# Solution 1
# Python

result=[0,0] # a list to store the winner's number and score
max=0

for i in range(5) :
    person=sum([int(x) for x in input().split()]) # Input the four scores of the participant and calculate the total score
    if max <= person : # if the total score is higher than the maximum score, 
        max= person # replace 'max' with the new total score
        result=[i+1, person] # store the result 

print("%d %d"%(result[0], result[1]))
