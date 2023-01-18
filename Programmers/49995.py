# https://school.programmers.co.kr/learn/courses/30/lessons/49995
# Solution 1
# Python

def solution(cookie) :
    answer = 0
    n = len(cookie)

    for i in range(n-1) :
        left_sum, left_idx = cookie[i], i
        right_sum, right_idx = cookie[i+1], i+1

        while True :
            if left_sum == right_sum :
                answer = max(answer, left_sum)
            if left_idx > 0 and left_sum <= right_sum :
                left_idx -= 1
                left_sum += cookie[left_idx]
            elif right_idx < n-1 and right_sum <= left_sum :
                right_idx += 1
                right_sum += cookie[right_idx]
            else :
                break
    return answer 

print(solution([1,1,2,3]))
print(solution([1,2,4,5]))
print(solution([1,2,2,5]))
print(solution([1,2,3,4,5,6,7]))