# 우주괴물

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: # 시작점
                for m in range(4):
                    k = 1 # 거리
                    while True:
                        ni = i+dr[m]*k
                        nj = j+dc[m]*k
                        if ni >= 0 and nj >= 0:
                            arr[ni][nj] = 1
                        else:
                            break
                        
    print(f'{tc} {count}')
    
    
    # 2를 찾아 ..?  괴물 위치가 시작점
    # 시작점 기준으로 상하좌우를 1로 바꿔 > 어떻게 ???
        # 열 : 0을 싹다 1로
        # 행 : 시작점 기준 좌에 0이 있으면 1로
                # 근데 1을 만나면 break
    # 0을 카운트 ..