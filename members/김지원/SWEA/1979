T =int(input())

for tc in range(T):
        
    N,K = map(int,input().split())

    matrix = [list(map(int,input().split())) for _ in range(N)]

    word_count = 0

    for i in range(N):
        count = 0
        for j in range(N):
            if matrix[i][j] == 1:
                count += 1
                if j == N-1 and count == K:
                    word_count += 1
            
            if matrix[i][j] == 0:
                if count == K:
                    word_count +=1
                    count = 0
                else:
                    count = 0

    for j in range(N):
        col_count = 0
        for i in range(N):
            if matrix[i][j] == 1:
                col_count += 1
                if i == N-1 and col_count == K:
                    word_count += 1
            
            if matrix[i][j] == 0:
                if col_count == K:
                    word_count +=1
                    col_count = 0
                else:
                    col_count = 0
     


    print(f'#{tc+1} {word_count}')
