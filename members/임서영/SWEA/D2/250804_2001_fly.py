T = int(input())
  
for tc in range(T):
    N, M = map(int, input().split())
  
    matrix = []
  
    # 행렬에 파리 값 저장
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
  
    max_dead_fly = 0
    # N*N의 범위(M값 빼줌)
    for x in range(N - M + 1):
        for y in range(N - M + 1):
            dead_fly = 0
            # M*M 파리채 한 대
            for i in range(x, x+M):
                for j in range(y, y+M):
                    dead_fly += matrix[i][j]
  
            if dead_fly > max_dead_fly:
                max_dead_fly = dead_fly
  
  
    print(f'#{tc+1} {max_dead_fly}')