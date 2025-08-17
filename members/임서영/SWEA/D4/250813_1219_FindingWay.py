T = 10

def dfs(node):
    global answer
    if node == 99:
        answer = 1
        return
    
    for next_node in adj_list[node]:
        # 방문했으면 뛰어넘기
        if visited[next_node]:
            continue
        # 아니면 방문체크
        visited[next_node] = 1
        dfs(next_node)
        visited[next_node] = 0


for tc in range(1, T+1):
    _, M = map(int, input().split())
    info = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)] #0~99까지 리스트가 있게 하기 위해서
    answer = 0
    visited = [0]*100

    for i in range(M):
        a = info[2*i]
        b = info[2*i+1]

        adj_list[a].append(b) #무향그래프면 양쪽 다 해줘야함!

    visited[0] = 1
    dfs(0)
    visited[0] = 0

    print(f'#{tc} {answer}')




########내꺼
from collections import defaultdict

def DFS(graph):
    start, target = 0, 99
    visited = set()
    stack = []
    

    def dfs(v):
        if v == target:
            return 1

        visited.append(start)

        for node in graph[start]:
            if node not in visited:
                dfs(start)
    
    return 0

T = 1
for tc in range(1, T+1):
    i, N = map(int, input().split())
    road = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(0, N*2, 2):
        graph[road[i]].append(road[i+1])
    
    print(f'#{tc} {DFS(graph)}')
