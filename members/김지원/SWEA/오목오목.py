T= int(input())
 
for tc in range(T):
    N = int(input())
 
    matrix = [list(input()) for _ in range(N)]
 
    dx = [1,0,-1,0,1,1]
    dy = [0,1,0,-1,1,-1]
 
    answer = 'NO'
 
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'o':
                for n in range(6):
                    count = 1
                    for k in range(1,N):
                        x_move = i + k*dx[n]
                        y_move = j + k*dy[n]
                        if 0 <= x_move < N and 0 <= y_move < N:
                            if matrix[x_move][y_move] == 'o':
                                count += 1
 
                                if count ==  5:
                                    answer = 'YES'
                                    break
                                 
                            else:
                                break
 
                if answer == 'YES':
                    break
 
        if answer == 'YES':
            break
 
    print(f'#{tc+1} {answer}')
