# https://www.acmicpc.net/problem/8958 
# Solution 1
# Python

num=int(input())

res_list=[] # a list to store the result for each input

for i in range(num) :
    ox_list = list(input())
    score = 0 # the score for the consecutive 'O's
    sum_score = 0 # the total score for the input
    for ox in ox_list : # for each character in 'ox_list'
        if ox == "O" : # if 'O' is found,
            score+=1 # increase 'score' (the value is accumulated if consecutive 'O's are found)
            sum_score+=score # add 'score' to 'sum_score'
        else :
            score=0 # set the 'score' back to zero
    res_list.append(sum_score)

for i in range(num) :
    print(res_list[i])