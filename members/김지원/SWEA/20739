T =int(input())

for tc in range(T):
        
    N,M = map(int,input().split())

    matrix = [list(map(int,input().split())) for _ in range(N)]

    max_count = 0

    for i in range(N):
        count = 0
        for j in range(M):
            if matrix[i][j] == 1:
                count += 1
                if j == N-1:
                    if max_count < count:
                        max_count = count

            
            if matrix[i][j] == 0:
                if max_count < count:
                    max_count = count
                count = 0

    for j in range(N):
        col_count = 0
        for i in range(M):
            if matrix[i][j] == 1:
                col_count += 1
                if i == M-1:
                    if max_count < col_count:
                        max_count = col_count

            
            if matrix[i][j] == 0:
                if max_count < col_count:
                    max_count = col_count
                col_count = 0


    print(f'#{tc+1} {max_count}')
