T = int(input())

def n_queen(row):
    global answer
    if row == N:
        answer += 1
        return
    
    for col in range(N):
        if not col_visited[col] and not ldiag_visited[row+col] and not rdiag_visited[row-col+N-1]:
            col_visited[col] = 1
            ldiag_visited[row+col] = 1
            rdiag_visited[row-col+N-1] = 1

            n_queen(row+1)

            col_visited[col] = 0
            ldiag_visited[row+col] = 0
            rdiag_visited[row-col+N-1] = 0
    
    return


for tc in range(1, T+1):
    N = int(input())
    col_visited = [0]*N
    ldiag_visited = [0]*(2*N-1)
    rdiag_visited = [0]*(2*N-1)
    answer = 0

    n_queen(0)

    print(f'#{tc} {answer}')

    