# DFS와 BFS 비교
# 양방향 연결 문제
# 함수는 제일 마지막에 짜야함

def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    v[c] = 1 # 방문체크

    for n in adj[c]: # 순서대로 꺼내기 3의 1꺼내지고 4꺼내지는거임
        if not v[n]: # 다음 노드에 방문하지 않았다면
            dfs(n)

def bfs(s):
    q = [] # 필요한 q, v[], 변수 생성

    q.append(s) # Q에 초기 데이터(들) 삽입
    ans_bfs.append(s) # 방문 데이터 추가
    v[s] = 1 # 방문 체크

    while q : # Q에 데이터가 있는 동안
        c = q.pop(0) # Q에서 데이터 하나 빼주고
        for n in adj[c]:
            if not v[n]: # 방문하지 않은 노드라면
                q.append(n) # Q에 삽입해라
                ans_bfs.append(n) 
                v[n] = 1 # 방문했당 표시


# 기본 입력값
N, M, V = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M): # 두개씩 연결된 숫자 받는거니까
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s) # 양뱡향

# 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

v = [0]* (N+1)
ans_dfs = []
dfs(V)

v = [0]* (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)