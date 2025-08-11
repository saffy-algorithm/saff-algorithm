T = int(input())

for t in range(1, T + 1):
    N = int(input())
    balloons = [list(map(int, input().split())) for _ in range(N)]

    row_sum = [0] * N
    col_sum = [0] * N

    # 행 합, 열 합 각각 계산
    for r in range(N):
        for c in range(N):
            row_sum[r] += balloons[r][c]
            col_sum[c] += balloons[r][c]

    ans = 0
    for r in range(N):
        for c in range(N):
            total = row_sum[r] + col_sum[c] - balloons[r][c]
            if total > ans:
                ans = total

    print(f'#{t} {ans}')
