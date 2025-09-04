# 단지 번호 붙이기

from collections import deque

def bfs(si, sj):
    q = deque() # 갈 곳을 저장하는 곳
    q.append([si, sj]) # 출발지 넣음
    
    v[si][sj] = 1
    cnt = 1

    while q: # q가 없을 때까지 돌거다
        cur_r, cur_c = q.popleft() # 현재 시작점 저장
    
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            # 범위 체크 (범위 안에 있어야함)
            # arr가 1일 때(집이 있어야되고), v가 0일 때(방문하지 않았을 때)
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and v[nr][nc] == 0:
                q.append([nr, nc])
                v[nr][nc] = 1
                cnt += 1

    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0] * N for _ in range(N)] # 방문체크 해야돼서 배열 크기가 똑같아야함

# 상하우좌
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] == 0:
            ans.append(bfs(i,j))

ans.sort()
# 단지 수는 ans의 길이, ans
print(len(ans))
for a in ans:
    print(a)