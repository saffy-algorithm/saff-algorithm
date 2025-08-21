# visited 생성
# 큐 생성, 시작점 인큐 -> 인덱스가 되면 됨 (4,3)
# 인큐 표시 -> visited도 2차원으로 만들어
# 반복

    # 디큐
    # 방문해서 할 일 -> if maze[i][j] == 3
    # 방문 정점에 인접하고 미방문이면
    
        # 인큐 -> 벽이 아니고, visited[ni][nj] == 0
        # 인큐 표시


# def bfs(i, j, N):
#     # 준비
#     visited = [[0]*N for _ in range(N)] # visited 생성
#     q = []      # 큐생성
#     q.append([i,j])# 시작점 인큐
#     visited[i][j] = 1# 시작점 인큐 표시
#     # 탐색
#     while q:
#         ti, tj = q.pop(0)   # 디큐
#         if maze[ti][tj] == 3:   # visit(t)
#             return visited[ti][tj] - 1 - 1 # 경로의 빈칸 수, -1 추가
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 미로내부고, 인접이고 벽이아니면,
#             wi, wj = ti+di, tj+dj
#             if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
#                 q.append([wi, wj])# 인큐
#                 visited[wi][wj] = visited[ti][tj] + 1   # 인큐 표시
#     return 0

# def find_start(N):
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 return i, j

# T = int(input())
# for tc in range(1, T+1):
    
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(N)]
#     sti, stj = find_start(N)
#     ans = bfs(sti, stj, N)
#     print(f'#{tc} {ans}')

##################################################################

# 경로로 접근 -> 라이브 강사님
# (visited 사용 안 하고) 변수 하나만 사용 -> 영원 강사님

# 강사님 코드
 
from collections import deque
 
dr = [-1, 1, 0, 0]
dc = [ 0, 0, -1, 1]
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    graph = []
    answer = -1 # 도착까지 가는데 만나는 0의 수
    # 도착까지 가는 경로의 수
    # 도착까지 가는데 걸리는 걸음 수
    # 도착까지 가는데 만나는 0의 수
 
    # 위 3개는 답이 다 달라
 
    # 입력과 동시에 출발의 위치를 찾고 싶은 것
    start_r , start_c = -1, -1
    for r in range(N):
        temp = list(map(int,input())) # temp 속에 2 가 있는지 없는 궁금함.
        for c in range(N):
            if temp[c] == 2:
                start_r = r
                start_c = c
        graph.append(temp)
     
    # BFS 탐색(이유: 최단경로)
 
    visited = [[0]*N for _ in range(N)]
    q = deque() 
     
    # 튜플. 데이터로 전송할 때 리스트보다 튜플이 빠름.    
    # 시작점은 변할 일이 없기 때문에 ?
    q.append((start_r,(start_c)))
    visited[start_r][start_c] = 1
 
    flag = False # 찾으면 나가고 싶음
 
    while q:
         
        answer += 1
 
        for _ in range(len(q)):
            r, c = q.popleft() # q는 방문대기열이니까 갈 수 있는 다음 지점을 찾아야 함
 
            for dir in range(4):
                next_r = r + dr[dir]
                next_c = c + dc[dir]
 
                # 아래의 조건을 만족하면 가라
                # 1. 맵 안쪽이어야 한다
                # 2. 1이 아니어야 한다.
                # 3. 방문 안했어야 한다
                # if 0<=next_r<N and 0<=next_c<N and graph[next_r][next_c] != 1 and not visited:
 
                # 위 조건 중 하나라도 만족하지 않으면 가지 마라
 
                # 이 중 하나라도 만족하면 다음 방향을 보세요
                # 1. 맵 바깥쪽이거나
                # 2. 1이거나
                # 3. 방문했거나
                if next_r<0 or next_c<0 or next_r>=N or next_c >= N or graph[next_r][next_c] == 1 or visited[next_r][next_c]:
                    continue
 
                if graph[next_r][next_c] == 3:
                    flag = True
                    break
 
                visited[next_r][next_c] = 1
                q.append((next_r, next_c))
 
        if flag:
            break
 
    if not flag:
        answer = 0
 
    print(f'#{tc} {answer}')


##################################################################

def bfs(i, j, N):
    # 1. 방문 체크용 배열 생성 (0: 미방문, >0: 방문 순서)
    visited = [[0]*N for _ in range(N)]
    # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    
    # 2. 큐 생성 (BFS는 큐 자료구조 사용)
    q = []      
    
    # 3. 시작점을 큐에 넣고 방문 표시 (거리 = 1로 시작)
    q.append([i, j])
    visited[i][j] = 1

    # 4. 큐가 빌 때까지 탐색
    while q:
        # (4-1) 큐에서 하나 꺼냄 (현재 위치)
        ti, tj = q.pop(0)   
        
        # (4-2) 도착점(3)에 도달했으면 경로 길이 계산
        if maze[ti][tj] == 3:
            # visited[ti][tj] 값은 시작점에서 현재 위치까지의 이동 칸 수 + 1
            # -1: 시작점을 뺌, 또 -1: 도착점도 뺌 → 중간 '빈 칸'만 계산
            return visited[ti][tj] - 1 - 1 
        
        # (4-3) 상하좌우 인접 칸 확인
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti+di, tj+dj
            
            # 미로 범위 안에 있고, 벽(1)이 아니며, 아직 방문 안 한 곳이면
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                # 큐에 추가
                q.append([wi, wj])
                # 방문 표시 (이전 거리 + 1)
                visited[wi][wj] = visited[ti][tj] + 1   

    # 도착점(3)에 도달하지 못한 경우 → 경로 없음
    return 0


def find_start(N):
    # 미로에서 출발점(2)의 좌표를 찾는 함수
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


# 테케 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    
    # 출발점 좌표 찾기
    sti, stj = find_start(N)
    
    # BFS 실행 후 결과 받기
    ans = bfs(sti, stj, N)
    
    # 결과 출력
    print(f'#{tc} {ans}')