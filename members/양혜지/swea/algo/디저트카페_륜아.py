# 아이디어
# 대각선 4개 전부 이용
# 

T = int(input())

# 처음 위치 계속 저장 : 
def dfs(i, j, x, y, order, cnt):
    global answer
    
    # 범위 밖으로 넘어가면 리턴
    if x < 0 or x >= N or y < 0 or y >= N:
        return
     
    # 처음위치와 같을 때
    if i == x and j == y:
        # 한바퀴 돌았네 ?
        if order == 4:
            answer = max(answer, cnt)
            return
 
    # 제자리가 아닌 경우에만 살펴보겠다
    else:
        if raw[x][y] in path:
            return
 
 
    path.append(raw[x][y])
 
    # 오차 범위 1일때만 갈거다
    if order <= 1:
        dfs(i, j, x+1, y+1, 1, cnt+1)
 
    if 1 <= order <= 2:
        dfs(i, j, x+1, y-1, 2, cnt+1)
 
    if 2 <= order <= 3:
        dfs(i, j, x-1, y-1, 3, cnt+1)
 
    if 3 <= order <= 4:
        dfs(i, j, x-1, y+1, 4, cnt+1)
    
    # 원복시켜주기 위해서 pop
    path.pop()
 
 
for tc in range(1, T+1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
 
    answer = -1
 
    for i in range(N):
        for j in range(N):
            path = []
            # 처음 위치, 대각선 넘버 <- order / cnt = 가장 많이 먹은 디저트 수 카운트
            dfs(i, j, i, j, 0, 0)
     
    print(f"#{tc} {answer}")