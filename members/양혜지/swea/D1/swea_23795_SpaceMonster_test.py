T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int(input().split()))) for _ in range(N)]
    cnt = 0

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]


    # 괴물의 시작점
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                mi = i
                mj = j

    # 괴물이 닿는 범위
    for d in range(4):
        # 거리
        step = 1
        while 0 <= (mi + dr[d]*step) < N and 0 <= (mj + dc[d]*step) < N and arr[mi+dr[d]*step][mj+dc[d]*step] == 0:
            arr[mi+dr[d]*step][mj+dc[d]*step] = 1
            step +=1

    for i in range(N):
        for j in range(N):
            # 인덱스에 접근
            if arr[i][j] == 0:
                cnt+=1
            
    print(f'#{tc} {cnt}')