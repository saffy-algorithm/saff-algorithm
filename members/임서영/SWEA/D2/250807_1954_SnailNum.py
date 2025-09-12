T = int(input())
 
for tc in range(T):
    N = int(input())
 
    snail = [[0]*N for _ in range(N)] 
 
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
 
    x = 0
    y = 0
    delta = 0
 
    for move in range(1, N*N+1):
        snail[x][y] = move
        nx = x + di[delta]
        ny = y + dj[delta]
 
        if nx >= N or nx < 0 or ny >= N or ny < 0 or snail[nx][ny] != 0:
            delta = (delta + 1) % 4
            nx = x + di[delta]
            ny = y + dj[delta]
         
        x = nx
        y = ny
 
    print(f'#{tc+1}')
    for i in snail:
        print(*i)