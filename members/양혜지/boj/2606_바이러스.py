# dfs를 하든 bfs를 하든
# 마지막에 비지티드 돌면서 방문한 정잠 표시 다 끝났을 때 마지막 비지티드 확인
# 순회하고 상태체크

def bfs():
    q = []
    q.append(1)     # 초기 데이터 삽입
    visited[1] = 1  # 1부터 방문 체크
    cnt = 0
    
    while q: # q에 데이터가 있는동안
        cur = q.pop(0)
        cnt +=1
        for next in adj[cur]:
            if not visited[next]: # 방문 검사
                visited[next] = 1 # 방문 체크
                q.append(next)                                                                                                                                                                                     \
    return (cnt -1)


N = int(input()) # 컴퓨터의 수 (노드의 수)
computer = int(input()) # 직접 연결되어있는 컴퓨터의 쌍의 수
adj = [[] for _ in range(N + 1)]

visited = [0] * (N+1)

for i in range(computer):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

answer = bfs()
print(answer)