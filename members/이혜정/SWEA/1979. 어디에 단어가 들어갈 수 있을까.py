T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    # 행 검사
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
            if arr[r][c] == 0 or c == N - 1:  # 구간 종료 조건
                if cnt == K:
                    answer += 1
                cnt = 0

    # 열 검사
    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
            if arr[r][c] == 0 or r == N - 1:  # 구간 종료 조건
                if cnt == K:
                    answer += 1
                cnt = 0

    print(f'#{tc} {answer}')
