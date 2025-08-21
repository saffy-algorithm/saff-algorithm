# visited 생성
# 큐 생성, 시작점 인큐 -> 인덱스가 되면 됨 (4,3)
# 인큐 표시 -> visited도 2차원으로 만들어
# 반복

    # 디큐
    # 방문해서 할 일 -> if maze[i][j] == 3
    # 방문 정점에 인접하고 미방문이면
    
        # 인큐 -> 벽이 아니고, visited[ni][nj] == 0
        # 인큐 표시
        
        
from collections import deque # collections 라이브러리에 덱 함수를 불러왔다(import)

def escape(maze): # 함수 선언
    n = 16 # 16*16
    visited = [[False] * 16 for _ in range(16)] # 방문체크 
    q = deque() # 큐는 선입선출-> 먼저 들어간게 먼저 나오는
    q.append(start) # q에 start를 append
    visited[start[0]][start[1]] = True # start[i][j]가 이미 방문한거면
    while q: # q를 계속돌아
        x, y = q.popleft() # x, y는 q에서 왼쪽에 있는 거
        
        if (x, y) == end: # x,y가 도착과 같다면
            return True # True를 반환
        
        # 상하좌우 돌기
        for i in range(4):
            # 다음 x, 다음y = x좌표에서 dx[i]만큼 간 거, y좌표에서 dy[i]만큼 간 거
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 다음x랑 다음y가 0보다 크거나 같고, n보다 작아야함(배열을 벗어나면 안돼서)
                if not visited[nx][ny] and maze[nx][ny] != 1: # visited[nx][ny]가 아니거나, maze[nx][ny]가 1이 아니면
                    visited[nx][ny] = True # visited[nx][ny]는 True
                    q.append((nx, ny))
    return False
    
T = 10 # 테스트케이스 10개
dx = [-1, 1, 0, 0] # 좌 우 상 하
dy = [0, 0, -1, 1]

for tc in range(1, T + 1): # tc 돌면서
    input() # 필요 없는 데이터 받기
    maze = [list(map(int, input())) for _ in range(16)] # 2차원 배열로 미로 입력 받기
    
    # 16*16 행렬 돌기
    for i in range(16):
        for j in range(16):
            # 시작점 찾기
            if maze[i][j] == 2: #maze[i][j]가 2면
                start = (i, j) # 시작점이 i,j다
            # 도착점 찾기
            elif maze[i][j] == 3: # maze[i][j]가 3이면
                end = (i, j) # 도착점이 i,j다
                
    if escape(maze):
        answer = 1 # 시작->출발 도달 가능시 1
    else:
        answer = 0 # 시작-> 출발 도달 불가능시 0
    print(f'#{tc} {answer}')

    