T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    cnt = 0
    
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    
    # 괴물이 서있는 곳이 시작점
    # 괴물은 2잖아 . . 2면 시작점이다
    
    # 시작점 기준으로 행이랑 열 1을 만나기 전까지 다 1로 바꿔
    # 1을 만나면 종료
    # 행이랑 열로 가려면 얼만큼 가야하는지 ? 거리 ?? k
    
    # 남은 0의 수 카운트
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:# 시작점
                # i,j 위치(인덱스) 기억을 해야해
                mi = i
                mj = j
                
    # 괴물이 닿는 범위
    for d in range(4):
        step = 1 # 초기값
        # 세가지 조건이 다 참일 때 while문이 돌아
        while 0 <= (mi + dr[d]*step) < N and 0 <= (mj + dc[d]*step) < N and arr[mi+dr[d]*step][mj+dc[d]*step] == 0:
            arr[mi+dr[d]*step][mj+dc[d]*step] = 1
            step +=1
            
    for i in range(N):
        for j in range(N):
            # 인덱스에 접근
            if arr[i][j] == 0:
                cnt+=1
            
    print(f'#{tc} {cnt}')
        
    
    # 행이랑 열 1을 만나기 전까지 다 1로 바꾸고
    # 1을 만나면 종료
    
    
    
    
    
    