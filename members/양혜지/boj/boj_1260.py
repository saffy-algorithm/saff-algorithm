# dfs bfs 비교
# 양방향 연결
# 함수는 제일 마지막에 쓰기

def dfs(c): # 현재 노드
    dfs_ans.append(c)
    v[c] = 1

    # 다음노드
    for n in adj[c]: # 순서대로 다음 노드 꺼내 3의 1 꺼내고 4 꺼내
        if not adj[c]: # 다음 노드에 현재 노드 방문 안 했으면
            dfs(n) # 다음 노드가 dfs 되는거지


N, M, K = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

# 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

v = [0] * (N+1)
dfs_ans = []
dfs(v)

v = [0] * (N+1)
bfs_ans = []
bfs(v)

print(*dfs_ans)
print(*bfs_ans)