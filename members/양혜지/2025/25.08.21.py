# def bfs(G, v): # 그래프 G, 탐색 시작점 v
#     visited = [0]*(n+1) # n : 정점의 개수
#     queue = [] # 큐 생성
#     queue.append(v) # 시작점 v를 큐에 삽입
#     visited[v] = 1 
    
#     while queue : # 큐가 비어있지 않은 경우
#         t = queue.pop(0) # 큐의 첫번째 원소 반환
#         visited(t)
        
#         for i in G[t]: # t와 연결된 모든 정점에 대해
#             if not visited[i]: # 인큐되지 않은 곳이라면
#                 queue.append[i] # 큐에 넣기
#                 visited[i] = visited[t] + 1 # n으로 부터 1만큼 이동
                
                
def bfs(s, V):
    # 초기화
    visited = [0] * (V + 1)     # visited 생성
    q = [s]                     # 큐 생성
                                # 시작점 인큐
    visited[s] = 1              # 인큐와 동시에 시작점 인큐 표시
    
    # 반복
    while q : # 탐색할 정점이 남아 있으면
        t = q.pop(0) # 디큐
        print(t)     # visit(), 방문정점 출력
        for w in adj_lst[t]: # 인접하고 미방문인 정점 인큐, 인큐 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
   
V, E = map(int,input().split()) # 마지막 정점, 간선 수
arr = list(map(int,input().split()))

# 인접 리스트
adj_lst = [[] for _ in range(V+1)] # V번행까지 준비
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1) # 방향 표시가 없는 경우 / v2에서 v1도 인접이야
    
bfs(1, V)

# 1 에서 각 정점까지 최소거리(간선 수)의 합은 ?

# 예제 5106 / 10966