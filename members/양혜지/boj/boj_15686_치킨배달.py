# 1부터 시작
# 치킨집의 최대 개수

# M : 폐업시키지 않을 치킨집 최대 개수
# 출력 : 도시의 치킨 거리의 최솟값
# 도시의 치킨 거리 : 모든 집의 치킨 거리의 합
# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리

# 어떤 경우에 안 뽑아도 되는지
# ㄴ 치킨 거리는 중도 포기가 불가능 

# (단순거리의) 이중포문

from itertools import combinations

N, M = map(int,input().split())

graph = [[0] * N for _ in range(N)]

home_rcs = []
store_rcs = []
answer = float('inf')

for r in range(N):
    row = list(map(int,input().split()))

    for c in range(N):
        graph[r][c] = row[c]

        if graph[r][c] == 1:
            home_rcs.append((r,c))
        elif graph[r][c] == 2:
            store_rcs.append((r,c))

distances = [[0] * len(store_rcs) for _ in range(len(home_rcs))]

for home_idx in range(len(home_rcs)):
    for store_idx in range(len(store_rcs)):

        distances[home_idx][store_idx] = abs(home_rcs[home_idx][0]-store_rcs[store_idx][0]) + abs(home_rcs[home_idx][1]-store_rcs[store_idx][1])

# list(combinations(range(len(store_rcs)) , M)) 절대 쓰지 말아라
for store_idx_set in combinations(range(len(store_rcs)) , M):

    # 해당 집 번호에서 갈 수 있는 치킨 거리 초기화
    distances = 0
    for home_idx in range(len(home_rcs)):
        min_distance = 2*(N-1) # float('inf')

        for store_idx in store_idx_set:
            min_distance = min(min_distance, abs(home_rcs[home_idx][0]-store_rcs[store_idx][0]) + abs(home_rcs[home_idx][1]-store_rcs[store_idx][1]))
        distances += min_distance

    # 해당 조합에 대한 치킨 거리
    # 다른 조합과도 비교해줘야함
    answer = min(answer, distances)

print(answer)

#######################################################################################
# (조합했다고 치고) BFS

# from itertools import combinations
# from collections import deque

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# def bfs():
#     q = deque()
#     visited = [[2*(N-1)+1]*N for _ in range(N)]

#     # 시작점 큐에 추가 (치킨집 수만큼 q에 넣어줄거라는뜻, 초기 위치)
#     for store_idx in store_idx_set:
#         r, c = store_rcs[store_idx]
#         visited[r][c] = 0
#         q.append((r, c))
    
#     while q:
#         r, c = q.popleft()
        
#         for dir in range(4):
#             nr = r+dr[dir]
#             nc = c+dc[dir]
            
#             if nr < 0 or nr >= N or nc < 0 or nc >= N:
#                 continue
#             if visited[nr][nc] <= visited[r][c]+1:
#                 continue

#             visited[nr][nc] = visited[r][c]+1
#             q.append((nr, nc))
    
#     distance = 0
#     for r, c in home_rcs:
#         distance += visited[r][c]

#     return distance

# N, M = map(int, input().split())
# graph = [[0]*N for _ in range(N)]

# home_rcs = []
# store_rcs = []
# answer = float('inf')

# for r in range(N):
#     rcs = list(map(int, input().split()))
#     for c in range(N):
#         graph[r][c] = rcs[c]
#         if graph[r][c] == 1:
#             home_rcs.append((r, c))
#         elif graph[r][c] == 2:
#             store_rcs.append((r, c))

# for store_idx_set in combinations(range(len(store_rcs)), M):
    
#     answer = min(answer, bfs())

# print(answer)