# 호출횟수 = 방문하는 노드의 수
# 노드가  N개 일 때,
# BFS -> N번
# DFS -> N번

# 연산수가 차이가 안남, BFS 최단거리발견

# # dfs
# def dfs(node):
#     for next in adj_list[node]:
#         if visited[next]:
#             continue
#         visited[next] = 1
#         dfs(next)
 
# T = int(input())
 
# for tc in range(1, T+1):
#     answer = 0
 
#     N, M = map(int, input().split())
#     connections = list(map(int, input().split()))
#     adj_list = [[] for _ in range(N+1)]
#     visited = [0]*(N+1)
     
#     for i in range(M):
#         idx1 = i*2
#         idx2 = idx1 + 1
 
#         # 내가 연결하고 싶은 친구는 a와 b야
#         a = connections[idx1]
#         b = connections[idx2]
 
#         adj_list[a].append(b)
#         adj_list[b].append(a)
 
#     for node in range(1, N+1):
#         if visited[node]:
#             continue
         
#         answer += 1
#         visited[node] = 1
#         dfs(node)
     
#     print(f'#{tc} {answer}')



##################################################
# Union Find
# 유니온 파인드

# 노드 7개
# 유니온 부모의 개수가 답
# 경로 압축 -> find를 하면서 생기는 것
# find 가 되지 않은 녀석이 있어서 갱신이 안됨, 경로압축이 안돼 len(set)으로 찾을 수 없음


# x의 부모를 찾을 때까지 재귀로 들어가
def find_set(x):
    if x == parents[x]:
        return x
    
    # 부모도 갱신해주면서 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]


def union_set(x,y):
    # 각각의 부모를 찾는 게 우선
    x_parent = find_set(x)
    y_parent = find_set(y)

    # 병합 기준, 부모의 크기가 더 작은걸로
    if x_parent < y_parent:
        parents[y_parent] = x_parent
    elif x_parent > y_parent:
        parents[x_parent] = y_parent

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    conncetions = list(map(int, input().split()))

    # make - set
    parents = [i for i in range(N+1)]

    # 연결관계입력
    # 안해도 되고 그냥 유니온 하면 됨

    for i in range(1, M*2, 2):
        # 경로압축이 되리라는 보장은 없음.
        union_set(conncetions[i], conncetions[i-1])

        # find set 으로 경로 압축, 0번 인덱스는 노드가 아님 주의
    for node in range(1,N+1):
        find_set(node)
        # 모든 노드에 대한 경로압축 완료
        # 최대 높이가 2
    
    print(f"#{tc} {len(set(parents[1:]))}")




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
#     # set