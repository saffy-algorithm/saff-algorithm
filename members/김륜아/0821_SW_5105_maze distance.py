# 미로의 거리

# T = int(input())

# def BFS(i, j, N):
#     visited[i][j] = 1
#     q = [(i, j)]

#     while q:

#         check_i, check_j = q.pop(0)
        
#         # 네 방향 반복
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             move_i, move_j = check_i + di, check_j + dj

#             # N*N 안에 있으면서 아직 가지 않은 길을 찾아 감.
#             # 길이 여러 개가 나오더라도 for 문 돌릴 때 제일 짧은 길 먼저 채워질 것이다
#             if 0 <= move_i < N and 0 <= move_j < N and maze[move_i][move_j] != 1 and visited[move_i][move_j] == 0:
#                 # 갈 수 있는 길들을 q에 보관
#                 q.append((move_i, move_j))

#                 # 가는 길에 +1 로 채워서 count
#                 visited[move_i][move_j] = visited[check_i][check_j] + 1

#                 # 도착지 만나면 return
#                 if maze[move_i][move_j] == 3:
#                     # 출발지부터 1로 채워넣기 때문에 -2를 해야함
#                     return visited[move_i][move_j] - 2


# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(N)]

#     # 출발, 도착 인덱스 찾기
#     find = False
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 start_i = i
#                 start_j = j

#                 find = True
#                 break
#         if find:
#             break

#     # visited
#     visited = [[0] * N for _ in range(N)]

#     answer = BFS(start_i, start_j, N)
#     if not answer:
#         answer = 0
#     print(f"#{tc} {answer}")
    

# 강사님 풀이

from collections import deque

T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    graph = []
    answer = -1

    s_r, s_c = -1, -1
    for r in range(N):
        temp = list(map(int, input()))
        for c in range(N):
            if temp[c] == 2:
                s_r, s_c = r, c
        graph.append(temp)
    
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((s_r, s_c))
    visited[s_r][s_c] = 1
    flag = False

    while q:

        answer += 1

        for _ in range(len(q)):
            r, c = q.popleft()
            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]

                # 1. 맵 바깥쪽이거나
                # 2. 1이거나
                # 3. 방문했거나
                # 위 조건 중 하나라도 만족하면 다음 방향을 보세요

                if nr < 0 or nr >= N or nc < 0 or nc >= N or graph[nr][nc] == 1 or visited[nr][nc]:
                    continue
                
                if graph[nr][nc] == 3:
                    flag = True
                    break

                visited[nr][nc] = 1
                q.append((nr, nc))

            if flag:
                break
        if flag:
            break

    if not flag:
        answer = 0
    
    print(f"#{tc} {answer}")
