T = 10
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(maze, sx, sy):
    visited = [[0]*16 for _ in range(16)]
    queue = []
    queue.append((sx, sy))

    while queue:
        x, y = queue.pop(0)
        if maze[x][y] == 3:
            return 1
        
        if not visited[x][y]:
            visited[x][y] = 1

            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 16 and 0 <= ny < 16:
                    if maze[nx][ny] != 1 and not visited[nx][ny]:
                        queue.append((nx, ny))

    return 0


for tc in range(1, T+1):
    _ = int(input())
    maze = [list(map(int, input())) for i in range(16)]
    sx = sy = 1
    result = bfs(maze, sx, sy)

    print(f'#{tc} {result}')