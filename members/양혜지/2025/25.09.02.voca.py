T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_len = 0
    count_a = 0
    count_b = 0

    # 가로
    for i in range(N):
        for j in range(N):

            # 행을 돌면서 1을 만나면 len 에 누적
            if arr[i][j] == 1:
                arr_len += 1
            
            else:
                # 1이 아니면 0이니깐
                if arr_len == K:
                    count_a += 1
                arr_len = 0
                

            if j == N - 1:
                if K == arr_len:
                    count_a += 1
                arr_len = 0

    # 세로 때매 초기화
    arr_len = 0

    # 가로
    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                arr_len += 1
            else:
                if arr_len == K:
                    count_b += 1
                arr_len = 0 

            if i == N - 1:
                if K == arr_len:
                    count_b += 1
                arr_len = 0 

    answer = (count_a + count_b)
    print(f'#{tc} {answer}')