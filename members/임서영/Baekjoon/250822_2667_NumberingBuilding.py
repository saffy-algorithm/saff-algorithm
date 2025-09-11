from collections import deque

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def numbering_house(B):
    q = deque()
    apt = [] # 아파트당 집 수
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if B[i][j] == 1 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = 1
                cnt = 1

                while q:
                    x, y = q.popleft()
                    for dx, dy in dir:
                        nx = dx + x
                        ny = dy + y
                        if 0 <= nx < N and 0<= ny < N and not visited[nx][ny]:
                            if B[nx][ny] == 1:
                                q.append((nx, ny))
                                visited[nx][ny] = 1
                                cnt += 1

                apt.append(cnt)

    print(len(apt))
    for i in sorted(apt):
        print(i)


N = int(input())
apart = [list(map(int, input())) for _ in range(N)]

numbering_house(apart)