# def find_parent(parent, x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
        
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a !=b:
        parent[b] = a


T = int(input())
for rc in range(1, T+1):
    N, M = map(int, input().split())
    parent = [[] for _ in range(N+1)] # 인접리스트

    for _ in range(M):
        a, b = map(int, input().split())
        union(a,b)

    # 카운트


