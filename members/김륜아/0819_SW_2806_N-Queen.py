# N-Queen

# 강사님

T = int(input())

def n_queen(row):
    global answer
    if row == N:
        answer += 1
        return
    
    for col in range(N):
        # 세로 검사 통과 & 좌하향 통과 & 우하향 통과, 세 경우를 다 통과해야한다.
        if not col_visited[col] and not left_diag_visited[row - col + (N - 1)] and not right_diag_visited[row + col]:
            col_visited[col] = 1
            left_diag_visited[row - col + (N - 1)] = 1
            right_diag_visited[row + col] = 1

            n_queen(row + 1)

            col_visited[col] = 0
            left_diag_visited[row - col + (N - 1)] = 0
            right_diag_visited[row + col] = 0
    return


for tc in range(1, T+1):
    N = int(input())
    
    col_visited = [0] * N
    left_diag_visited = [0] * (2*N -1) # (2*N - 2) 까지 가야하기 때문에 (2*N - 1)로 설정
    right_diag_visited = [0] * (2*N -1)
    answer = 0

    n_queen(0)

    print(f"#{tc} {answer}")

