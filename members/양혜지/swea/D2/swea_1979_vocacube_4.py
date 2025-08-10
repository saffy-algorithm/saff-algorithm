T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer =  0
    
    for r in range(N):
        recent_c = -1
        for c in range(N):
            if graph[r][c] ==0 :
                if c - recent_c -1 == K:
                    answer += 1
                recent_c = c # 0 을 만나면 무조건 수행, 초기화 이전에 돌아봐야함
                
        if N - recent_c -1 == K:
            answer += 1