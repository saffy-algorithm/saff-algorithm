from collections import deque

def tomato(t, sx, sy):
    global zero_count

    q = deque()
    for i in range(len(sx)):
        q.append((sx[i], sy[i]))

    step = -1
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            # 네 방향 탐색해서 다음 탐색지점 선정
            for dx, dy in dir:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < N and 0 <= ny < M:
                    if t[nx][ny] == 0:
                        zero_count -= 1
                        t[nx][ny] = 1
                        q.append((nx, ny))
        step += 1

    if zero_count != 0:
        return -1
    else:
        return step


M, N = map(int, input().split())
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
tomatoes= []

sx = []
sy = []
zero_count = 0

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 1:
            sx.append(i)
            sy.append(j)
        elif temp[j] == 0:
            zero_count += 1
    tomatoes.append(temp)

result = tomato(tomatoes, sx, sy)
print(result)