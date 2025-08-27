from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]
T = int(input())


for tc in range(1, 1+T):
    N = int(input())
    graph =[]
    answer = -1  # 경로 길이, 발자국 수, 중간 거리 다 초기값이 달라질 수 있다.
    s_r, s_c = -1, -1
    for r in range(N):
        temp = list(map(int, input()))
        for c in range(N):
            if temp[c] == 2:
                s_r, s_c = r, c
        graph.append(temp)
    
    #BFS로 짤겁니다. --> 최단경로 니까
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((s_r, s_c)) # 변경될 일이 없으니 튜플이 조금 더 합리적이다. 튜플이 리스트보다 전송이 빠르다
    visited[s_r][s_c] = 1

    flag = False # 만약 찾으면 q에 더 있던 말던 나가면 된다.

    while q: # 묶음 자료형은 비어 있으면 False가 된다. 즉, q가 빌때까지 돌아라, #4
        
        answer +=1 # 시작지점 q=1 for문은 1번 돌며 

        for _ in range(len(q)): # 3
            r, c = q.popleft()

            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]

                # 아래의 조건을 만족하면 가라  --> 이 중 하나라도 만족하면 다음 방향을 보세요
                # 1. 맵 안쪽이어야 한다. --> 맵 바깥쪽 이거나
                # 2. 1이 아니어야 한다. --> 1이거나
                # 3. 방문 안했어야 한다. --> 방문 했거나 

                # 위 조건 중 하나라도 만족하지 않으면 가지 마라
                if nr<0 or nr >=N or nc <0 or nc >=N or graph[nr][nc]==1 or visited[nr][nc]:
                    continue
                # 내려 왔다는 것은 위에 모두를 만족하니 방문해봄직 한 위치다.

                if graph[nr][nc] == 3:
                    flag = True
                    break

                visited[nr][nc] = 1
                q.append((nr, nc)) 
            if flag: #3
                break
        if flag: #4
            break
    
    if not flag:
        answer = 0
    print(f'#{tc} {answer}')
