# 숨바꼭질

from collections import deque

def BFS():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()

        if x == K:
            return visited[x]

        # 4방향 탐색과 똑같이 탐색
        for nx in [x-1, x+1, 2*x]:
            # visited[nx] == -1 조건을 걸어줌으로써 최단거리를 찾을 수 있다.
            if 0 <= nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)
                    

N, K = map(int, input().split())

# 방문 안 한 곳을 -1로 두기
# 첫 위치를 0으로 둘 것이기 때문에
visited = [-1] * (100001)
visited[N] = 0
time = BFS()


print(time)