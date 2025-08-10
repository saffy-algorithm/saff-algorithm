T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    flies = [list(map(int,input().split())) for _ in range (N)]
    answer = 0
    
    # 시작점 확정
    for r in range(N-M+1):
        for c in range(N-M+1):
            
            temp_sum = 0
            
            for i in range(M):
                for j in range(M):
                    flies[r+i][c+j]
                    temp_sum += flies[r+i][c+j]
            
            if answer < temp_sum:
                answer = temp_sum
            
            
            
            # j가 바뀔 때마다 갱신
            answer = max(answer, temp_sum)
        
    print(f'#{tc} {answer}')