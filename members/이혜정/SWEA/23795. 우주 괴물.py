T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dj = [0, 0, -1, 1]
    unsafe_cnt = 0
    one_cnt = 0

    # 우주괴물 위치
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                alien_x = i
                alien_y = j

    # 안전하지 않은 구역 카운트
    for d in range(4):
        for step in range(1, N):
            nx = alien_x + di[d] * step
            ny = alien_y + dj[d] * step
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 1:
                    break
                unsafe_cnt += 1

    # 벽 개수 카운트
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                one_cnt += 1

    print(f'#{tc} {N*N - unsafe_cnt - one_cnt - 1}')    # 전체 개수 - 안전하지 않은 구역 개수 - 벽 개수 - 우주괴물