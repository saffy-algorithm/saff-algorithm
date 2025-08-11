# N, M 주의, max_cnt가 1일 때 주의

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    photo = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    # 행 방향
    for r in range(N):
        row_cnt = 0
        for c in range(M):
            if photo[r][c] == 1:
                row_cnt += 1
                max_cnt = max(row_cnt, max_cnt)
            else:
                row_cnt = 0

    # 열 방향
    for c in range(M):
        col_cnt = 0
        for r in range(N):
            if photo[r][c] == 1:
                col_cnt += 1
                max_cnt = max(col_cnt, max_cnt)
            else:
                col_cnt = 0

    if max_cnt == 1:
        max_cnt = 0

    print(f'#{tc} {max_cnt}')