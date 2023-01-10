# https://www.acmicpc.net/problem/2775 
# Solution 1
# Python

T = int(input()) # T = 테스트 케이스 수 

for i in range(T) :
    k=int(input()) # k = 아파트 층
    n=int(input()) # n = 아파트 호
    f0=[x+1 for x in range(n)] # 0층에서 1호~n호까지 각각 거주자 수 조사
    for j in range(k) : # 각 층에 대해
        for z in range(1,n) : # 각 호에 대해
            f0[z]+=f0[z-1]
            # 2호라면, 바로 아래층의 1호 + 2호 
            # 3호라면, 바로 아래층의 2호 + 3호 
    print(f0[-1])

