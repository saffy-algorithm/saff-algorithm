# 풍선팡

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 리스트 컴프리헨션
    arr = [list(map(int, input().split())) for _ in range(N)]
     
    max_score = 0
     
    for i in range(N):
        for j in range(N):
            row_sum = sum(arr[i])

            # 리스트 컴프리헨션
            col_sum = sum(arr[k][j] for k in range(N))
            score = row_sum + col_sum - arr[i][j]
            max_score = max(max_score, score)
    print(f'#{tc} {max_score}')
