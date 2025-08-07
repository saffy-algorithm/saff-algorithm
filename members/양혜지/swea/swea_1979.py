# 연결된 숫자랑 K의 값이 동일해야함 ??? ?? ? .......

T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    arr_len = 0
    count_a = 0
    count_b = 0
    
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                arr_len +=1
            else:
                if K == arr_len:
                    count_a +=1
                arr_len = 0
                
            if j == N-1:
                if K == arr_len:
                    count_a +=1
                arr_len = 0
                
    for j in range(N):
        for i in range(N):
            if puzzle[i][j] == 1:
                arr_len +=1
            else:
                if K == arr_len:
                    count_b +=1
                arr_len = 0
                
            if i == N-1:
                if K == arr_len:
                    count_b +=1
                arr_len = 0
                
    answer = (count_a + count_b)
    print(f'#{tc} {answer}')