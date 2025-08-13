T= int(input())

for tc in range(T):

    N = int(input())

    matrix = [list(map(int,input().split())) for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                x_cor = i
                y_cor = j
                break

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for n in range(4):
        for m in range(1,N):
            x_move = x_cor + m*dx[n]
            y_move = y_cor + m*dy[n]
            if 0 <= x_move < N and  0 <= y_move < N :
                if matrix[x_move][y_move] == 0:
                    matrix[x_move][y_move] = 1

                else:
                    break

    count = 0
    for p in range(N):
        for q in range(N):
            if matrix[p][q] == 0:
                count += 1


    print(f'#{tc+1} {count}')

        
                

