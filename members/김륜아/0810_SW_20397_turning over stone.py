# 돌 뒤집기 게임2

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    raw = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
    
        for j_check in range(1, j+1):
            if (i-1) - j_check >= 0 and (i-1) + j_check < N:
                if raw[(i-1) - j_check] == raw[(i-1) + j_check]:
                    raw[(i-1) - j_check] = 1 - raw[(i-1) - j_check]
                    raw[(i-1) + j_check] = 1 - raw[(i-1) + j_check]
    
    print(f"#{tc}", end = ' ')
    print(*raw)