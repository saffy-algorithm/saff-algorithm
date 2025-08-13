# 고대 유물

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0

    for i in range(N):
        count = 0
        for j in range(M):
            if arr[i][j] == 1:
                count += 1
            else:
                if count >= 2:
                    max_len = max(max_len, count)
                count = 0
        if count >= 2:
            max_len = max(max_len, count)
            
    for j in range(M):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count >= 2:
                    max_len = max(max_len, count)
                count = 0
        if count >= 2:
            max_len = max(max_len, count)
    print(f'#{tc} {max_len}')