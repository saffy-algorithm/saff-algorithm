#   숫자 배열 회전

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]

    raw_90 = [[0]*N for _ in range(N)]
    raw_180 = [[0]*N for _ in range(N)]
    raw_270 = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            raw_90[j][(N-1)-i] = raw[i][j]
            raw_180[(N-1)-i][(N-1)-j] = raw[i][j]
            raw_270[(N-1)-j][i] = raw[i][j]
    

    answer = [[0]*3 for _ in range(N)]
    for j in range(3):
        for i in range(N):

            # 1열은 90도, 2열은 180도, 3열은 270도 회전 값들을 나열
            if j == 0:
                answer[i][j] = ''.join(map(str, raw_90[i]))
            if j == 1:
                answer[i][j] = ''.join(map(str, raw_180[i]))
            if j == 2:
                answer[i][j] = ''.join(map(str, raw_270[i]))

    print(f"#{tc}")
    for i in range(N):
        print(*answer[i])