# 단지 번호 붙이기

from collections import deque

def bfs(si, sj):
    q = deque()
    q.append([si, sj])
    
    v[si][sj] = 1
    cnt = 1

    while q: # q 끝날 때까지
        cur_r, cur_c = q.popleft()
    
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and v[nr][nc] == 0:
                q.append([nr, nc])
                v[nr][nc] = 1
                cnt += 1

    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0] * N for _ in range(N)] # 방문 체크를 배열 크기만큼 받야야함 -> 왜 ? -> 

# 상하우좌
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

ans = []
for i in range(N):
    for j in range(N): # 배열을 돌거야
        if arr[i][j] == 1 and v[i][j] == 0: # 방문 안 한 1이면서, 방문체크가 안된 0일 때
            temp = bfs(i,j)
            ans.append(temp) # 엔서에 어펜드 -> bfs 좌표 들어가야댐
# bfs 좌표 ? -> 
ans.sort()
print(len(ans))
for a in ans:
    print(a)