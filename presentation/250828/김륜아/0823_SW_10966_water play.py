# 물놀이를 가자

from collections import deque

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    raw = [input() for _ in range(N)]

    # 방문하지 않은 위치를 -1로 채우기
    q = deque()
    visited = [[-1]*M for _ in range(N)]

    # 모든 땅에서 제일 가까운 물까지 가는 step 수를 세는 것이 문제.
    # 물인 곳을 먼저 q에 append하고, 0으로 시작점 방문처리 해주기
    for i in range(N):
        for j in range(M):
            if raw[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0
    
    # 각 'W'에서 시작, 방문하지 않은 곳들을 차례대로 탐색해주기
    while q:
        i, j = q.popleft()
        for delta in range(4):
            ni = i + di[delta]
            nj = j + dj[delta]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
    
    answer = 0

    # 각 'L'위치의 visited값이 'W'까지 가는 스텝 수이다.
    # 각 visited값 더해주기
    for i in range(N):
        for j in range(M):
            if raw[i][j] == 'L':
                answer += visited[i][j]

    print(f"#{tc} {answer}")
