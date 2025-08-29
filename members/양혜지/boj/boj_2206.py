# 벽 부수기

from collections import deque

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[[0]*N for _ in range(N)] for _ in range(2)]

def bfs():
    
    q = deque()
    visited[0][0][0] = 1
    q.append(0, 0, 0) # k = 벽을 부순 횟수 / r,c 좌표
    
    # 도착지까지의 발걸음 수
    # 포함한 경로의 길이
    # 들어가자마자 스텝이 1이 된 셈
    step = 1
    # q에 들어있는 사이즈만큼만 돌았을 때
    while q : 
        
        # 현재 q의 길이만큼만 빼라
        for _ in range(len(q)):
            k, r, c = q.popleft()
            
            if r == N-1 and c == N-1:
                # 자기 위치가 1
                return step
            
            # 사방탐색
            for dir in range(4):
                nk = k
                nr = r + dr[dir]
                nc = c + dc[dir]
                
                # 다음 위치 탐색
                if nr < 0 or nr >= N or nc < 0 or nc >= M :
                    continue
                
                if graph[nr][nc] == 1:
                    if nk == 1 or visited[1][nr][nc]:
                        continue
                    nk = 1
                else:
                    if visited[nk][nr][nc]:
                        continue
                    
                    
                    
                    
        

print(bfs())