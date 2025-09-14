from collections import deque

def bfs(i, j):
    q = deque()
    # 행/열 좌표 두개가 필요함 
    # -> 안 묶으면 pop을 했을 때, 숫자가 하나만 나와서 묶어야댐 튜플로 ..
    q.append((i,j))
    # 1. 방문체크 2. 최단거리 카운트 용도
    visited = [[0] * N for _ in range(N)]
    # 중복 체크 / 다시 돌아오지마센
    visited[i][j] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] != 1:
                    if visited[nr][nc] == 0:
                        # 다음칸은 전칸보다 한칸 더 가야함
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr,nc))

    return visited[end_i][end_j]


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                # 시작점 찾기
                start_i = i
                start_j = j
            if arr[i][j] ==  3:
                # 도착점 찾기
                end_i = i
                end_j = j

    answer = bfs(start_i, start_j)
    if answer == 0 :
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {answer -2}')






    # 1. bfs를 돌 시작점이 필요
    # 2. 델타 선언
    # 