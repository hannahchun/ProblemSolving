# https://www.acmicpc.net/problem/10026 
# Python
# Solution 1

import sys
from collections import deque

def bfs(i, j, color, arr) :
    queue = deque()
    queue.append((i, j))
    arr[i][j] = 0 # 방문 처리

    while queue : # queue에 아무것도 없을 때까지 진행
        x, y = queue.popleft()
        for idx in range(4) : # 상, 하, 좌, 우에 같은 색깔이 있는지 확인 
            nx = x + dx[idx]
            ny = y + dy[idx]
            # 인덱스가 matrix의 범위를 벗어나면 제어흐름은 유지한 상태에서 나머지 코드의 실행만 건너뜀
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            # 같은 색일 경우 방문 처리하고 queue에 넣기
            if arr[nx][ny] == color :
                arr[nx][ny] = 0
                queue.append((nx, ny))


n = int(sys.stdin.readline())

# 적록색약이 아닌 matrix
matrix = [list(sys.stdin.readline()) for _ in range(n)] 

# 적록색약인 matrix
matrix_rg = [[0] * n for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if matrix[i][j] == 'R' or matrix[i][j] == 'G' :
            matrix_rg[i][j] = 'R'
        else :
            matrix_rg[i][j] = 'B'

# 총 구역의 개수 담기
answer = 0 # 적록색약이 아님
answer_rg = 0 # 적록색약임

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0] # x좌표 기준
dy = [0, 0, -1, 1] # y좌표 기준

# 총 구역의 개수 찾기
for i in range(n) :
    for j in range(n) :
        # 적록색약이 아님
        if matrix[i][j] != 0 : # 아직 처리가 안된 경우,
            bfs(i, j, matrix[i][j], matrix)
            answer += 1
        # 적록색약임
        if matrix_rg[i][j] != 0 : # 아직 처리가 안된 경우,
            bfs(i, j, matrix_rg[i][j], matrix_rg)
            answer_rg += 1

print(answer)
print(answer_rg)


"""

<입력 예시>
1. n = int(sys.stdin.readline()) 
-> n = 5 
2. matrix = [list(sys.stdin.readline()) for _ in range(n)]
-> RRRBB
   GGBBB
   BBBRR
   BBRRR
   RRRRR
   matrix = [['R', 'R', 'R', 'B', 'B', '\n'], ['G', 'G', 'B', 'B', 'B', '\n'], ['B', 'B', 'B', 'R', 'R', '\n'], ['B', 'B', 'R', 'R', 'R', '\n'], ['R', 'R', 'R', 'R', 'R', '\n']]

"""