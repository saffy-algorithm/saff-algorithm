# 우주 괴물

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
 
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                idx_i = i
                idx_j = j
 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
 
    for d in range(4):
        for step in range(1, N):
            di = idx_i + dx[d] * step
            dj = idx_j + dy[d] * step
            if 0 <= di < N and 0 <= dj < N:
                if arr[di][dj] == 1:
                    break
                else:
                    arr[di][dj] = 1
    for i in range(N):
        answer += arr[i].count(0)
     
    print(f'#{tc} {answer}')
                                 