def dfs(v):
    visited[v] = True
    for next in adj[v]:
        if not visited[next]:
            dfs(next) 
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    nums = list(map(int, input().split()))
    for i in range(0, len(nums), 2):
        a,b = nums[i],nums[i+1]
        adj[a].append(b)
        adj[b].append(a)
 
    visited = [False] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(f"#{tc} {cnt}")



# def find_parent(x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         parent[x] = find_parent(parent[x])
        
# def union(a, b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a !=b:
#         parent[b] = a


# T = int(input())
# for rc in range(1, T+1):
#     N, M = map(int, input().split())
#     parent = [[] for _ in range(N+1)] # 인접리스트

#     for _ in range(M):
#         a, b = map(int, input().split())
#         union(a,b)

#     # 카운트


