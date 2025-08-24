from collections import deque

T = int(input())
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(maze, sx, sy):
    visited = [[0]*N for _ in range(N)]
    queue = deque()
    queue.append((sx, sy, 0))

    while queue:
        x, y, d = queue.popleft()
        if maze[x][y] == 3:
            return d-1 #도착제외
        
        if not visited[x][y]:
            visited[x][y] = 1

            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if maze[nx][ny] != 1 and not visited[nx][ny]:
                        queue.append((nx, ny, d+1))

    return 0



for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sx = sy = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sx = i
                sy = j
                break
        if sx != -1:
            break

    result = bfs(maze, sx, sy)

    print(f'#{tc} {result}')