# https://www.acmicpc.net/problem/5355
# Solution 1
# Python

case = int(input())

for i in range(case) :
    answer = 0
    mars = list(map(str, input().split())) # store each element as a string type in a list using map()
    for j in range(len(mars)) :
        if j == 0 : 
            answer += float(mars[j]) # convert the first element into float type and store it in 'answer'
        else : # for each operation, calculate according to the given rule 
            if mars[j] == "@" :
                answer *= 3
            elif mars[j] == "%" :
                answer += 5
            elif mars[j] == "#" :
                answer -= 7
    print("%0.2f" % answer)
