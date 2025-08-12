# 어디에 단어가 들어갈 수 있을까

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    # 행 점검
    for i in range(N):
        for j in range(N-K+1):
            if raw[i][j:j+K] == [1] * K:
                if (j - 1 < 0 or raw[i][j-1] == 0) and (j + K >= N or raw[i][j+K] == 0):
                    count += 1
    
    # 열 점검

    raw_vertical = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            raw_vertical[i][j] = raw[j][i]

    for i in range(N):
        for j in range(N-K+1):
            if raw_vertical[i][j:j+K] == [1] * K:
                if (j - 1 < 0 or raw_vertical[i][j-1] == 0) and (j + K >= N or raw_vertical[i][j+K] == 0):
                    count += 1
        


    print(f"#{tc} {count}")
