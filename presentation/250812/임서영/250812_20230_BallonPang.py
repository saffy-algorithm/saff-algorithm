T = int(input())

for tc in range(T):
    N = int(input())
    Bals = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0

    for i in range(N):
        for j in range(N):
            row_score = sum(Bals[i])
            col_score = sum(Bals[r][j] for r in range(N))
            score = row_score + col_score - Bals[i][j]
            max_score = max(max_score, score)

    print(f'#{tc+1} {max_score}')