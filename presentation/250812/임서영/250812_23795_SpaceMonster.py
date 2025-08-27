T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]

    wall = 0

    for i in range(N):
        for j in range(N):
            # 몬스터 위치 찾으면 레이저 칸 세는 조건+반복문
            if space[i][j] == 2:
                x = i
                y = j
                rasor = 1 # 괴물 자리(레이저 자리는 아니지만 안전구역 제외를 위해 1)
                for delta in range(4):
                    for m in range(1, N+1):
                        nx = x + di[delta]*m
                        ny = y + dj[delta]*m
                        
                        # 범위 밖으로 가기 전까지 레이저 발사
                        if 0<=nx<N and 0<=ny<N:
                            #벽 만나면 레이저 쏘는거 break
                            if space[nx][ny] == 1:
                                break
                            rasor += 1
            
            # 벽 개수 세기
            if space[i][j] == 1:
                wall += 1
    
    result = N*N - wall - rasor
    print(f'#{tc} {result}')             