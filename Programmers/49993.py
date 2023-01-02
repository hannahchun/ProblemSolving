# https://school.programmers.co.kr/learn/courses/30/lessons/49993?language=python3
# Solution 1
# Python

def solution(skill, skill_trees) :
    answer = 0 # The possible number of answers
    valid = [skill] # The possible orders

    for i in range(len(skill)) :
        valid.append(skill[:i])
    
    for skill_tree in skill_trees : # For each 'skill_tree',
        # 1. Join together letters in 'skill' using join() (= Erase letters not in 'skill')
        # 2. Check whether the newly-formed word exists in 'valid'
        if ''.join([s for s in skill_tree if s in skill]) in valid :
            answer+=1
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
print(solution("AC", ["A", "CD", "BAC", "CA"]))