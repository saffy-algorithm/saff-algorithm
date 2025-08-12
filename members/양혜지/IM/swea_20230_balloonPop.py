T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_score = 0

    for i in range(N):
        for j in range(N):
            row_arr = sum(arr[i])
            col_arr = sum(arr[k][j] for k in range(N))
            score = row_arr + col_arr - arr[i][j]
            max_score = max(max_score, score)

    print(f'#{tc} {max_score}')

