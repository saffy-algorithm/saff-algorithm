# 토마토 

from collections import deque

# delta 방향
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

M, N = map(int,input().split()) # M : 열 개수, N : 행 갯수
tomato = [list(map(int, input().split())) for _ in range(N)]


# 익은 토마토 위치 리스트
tomato_idx = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            tomato_idx.append((i, j))

# 시작일을 -1로 돌아야 함
# 1. 토마톡 다 익어있는 경우에 while 한 바퀴 돌고 0을 출력해야 함
# 2. 정답이 8이 나와야 하는데, 마지막 익은 토마토가 append 돼서 while문을 한 바퀴 더 돌게 됨
days = -1

while tomato_idx:

    for _ in range (len(tomato_idx)):
        i, j = tomato_idx.popleft()
        for delta in range(4):
            ni = i + di[delta]
            nj = j + dj[delta]
            if 0 <= ni < N and 0 <= nj < M:
                if tomato[ni][nj] == 0:
                    tomato[ni][nj] = 1
                    tomato_idx.append((ni, nj))
                
    days += 1

# 토마토가 다 익을 수 없는 경우에는 days 가 -1로 나와야 함
find = False
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            days = -1
            find = True
            break
    if find:
        break

print(days)
