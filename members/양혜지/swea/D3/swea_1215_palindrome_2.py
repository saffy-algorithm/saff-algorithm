# 파리퇴치랑 비슷 ..

T = 30

for i in range(1, T+1):
    N = int(input())
    graph = [input() for _ in range(8)] # 8번 돈다 했으니
    answer = 0 # 발견된 게 없을거니까
    
    # 시작점 잡아야됨
    # 행열을 돌면서 잡아야겠죠
    # i가 행 -> 끝까지 가야됨
    # j가 열 -> skip이 가능 / n에 따라서 바뀔 수가 있음
    
    for i in range(N):
        for j in range(8-N+1):
            
            for k in range(N//2):
                # 이제 여기서 회문 검사
                # 앞 / 뒤
                # 시작점 j로부터 끝글자로 가고
                if graph[i][j+k] != graph[i][j+N-1-k]:
                    break
                
            else: # 안 걸릴 때만 들어옴
                answer += 1
                
            for k in range(N//2):
                if graph[j+k][i] != graph[j+N-1-k][i]:
                    break
                
            else:
                answer += 1